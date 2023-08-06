import json
import socket
import sys
from threading import Thread
from types import SimpleNamespace

from rich.console import Console
from rich.theme import Theme

from voxx.model import User, UID

UM_HANDLERS = dict()
console = Console(theme=Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
}))


class ResReqClient(socket.socket):
    def __int__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)

    def request(self, req: json) -> SimpleNamespace:
        req = f'{json.dumps(req)}\n'
        self.send(req.encode("utf-8"))
        data = self.recv(1024).decode("utf-8")
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


class UMClient(ResReqClient, Thread):
    def __init__(self, main_user: str, addr: tuple) -> None:
        ResReqClient.__init__(self)
        Thread.__init__(self)
        self.connect(addr)
        req = {"request-id": "su", "params": {"main-user": f'{main_user}'}}
        self.request(req)
        self._owning_instance = None
        self._on_close = None
        self.settimeout(None)
        keep_alive(self)

    def set_runner_instance(self, instance):
        self._owning_instance = instance

    def on_close(self, func):
        self._on_close = func

    def run(self):
        try:
            while (data := self.recv(1024).decode("utf-8")) is not None:
                msg = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
                console.log(msg)
                key = getattr(msg, 'update-message')
                if key in UM_HANDLERS:
                    func = UM_HANDLERS[key]
                    func(self._owning_instance, msg)
        except (ConnectionResetError, ConnectionAbortedError):
            if self._on_close is not None:
                self._on_close()
            self.close()


def keep_alive(sock: socket.socket):
    os = sys.platform
    if os == 'win32':
        sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
    elif os == 'linux':
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 3)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)
    elif os == 'darwin':
        tcp_ka = 0x10
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.setsockopt(socket.IPPROTO_TCP, tcp_ka, 3)


res_req_conn: ResReqClient
um_conn: UMClient

assoc_user: User


def um_handler(func):
    UM_HANDLERS[func.__name__] = func
    return func


def assert_rr(func):
    def wrapper(*args, **kwargs):
        try:
            if res_req_conn is None:
                console.print("Response-Request connection not established!", style="bold red")
                return
            return func(*args, **kwargs)
        except ConnectionResetError:
            return None

    return wrapper


@assert_rr
def ping() -> SimpleNamespace:
    return res_req_conn.request({"request-id": "ping"})


@assert_rr
def register_user(username: str) -> SimpleNamespace:
    return res_req_conn.request({"request-id": "ru", "params": {"uname": username}})


@assert_rr
def send_message(message='') -> SimpleNamespace:
    """Send message to server"""
    if message == '':
        return SimpleNamespace()
    return res_req_conn.request({'request-id': 'sm', 'params': {'message': f'{message}'}})


@assert_rr
def get_user_list() -> SimpleNamespace:
    return res_req_conn.request({'request-id': 'ul'})


@assert_rr
def close() -> None:
    res_req_conn.close()
    um_conn.close()


@assert_rr
def get_assoc_user():
    global assoc_user
    return assoc_user


def establish_voxx_connection(user: str, addr: tuple):
    global res_req_conn
    global um_conn
    global assoc_user
    try:
        res_req_conn = ResReqClient()
        res_req_conn.connect(addr)

        res = register_user(user)
        if getattr(res, 'response-id') == 0:
            console.print(f'Username [bold magenta]{user}[/bold magenta] is already taken!', style='bold red')
            sys.exit(1)
        uid_int = int(res.body.user.uid)
        assoc_user = User(UID.of(uid_int), res.body.user.uname)
        console.print(f'Connected to Voxx server as [bold magenta]{assoc_user.username}[/bold magenta]!', style='green')
        um_conn = UMClient(user, addr)
        um_conn.start()

    except (TimeoutError, InterruptedError, ConnectionRefusedError):
        console.print(f'Could not connect to Voxx server at {addr}!', style='bold red')
        sys.exit(1)
