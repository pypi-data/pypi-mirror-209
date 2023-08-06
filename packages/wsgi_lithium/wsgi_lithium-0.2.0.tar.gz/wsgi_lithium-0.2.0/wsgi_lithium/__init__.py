import getopt
from typing import Any, NoReturn, Union
import socket
import sys
from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
from .gunicorn_utils import import_app, parse_address, is_ipv6


class WSGIServer6(WSGIServer):
    address_family = socket.AF_INET6


USAGE: str = """\
Usage: {name:s} [-b ADDRESS | --bind ADDRESS] APPLICATION

ADDRESS:
    A string in HOST:PORT format, where HOST is a valid IP address and PORT is a
    valid TCP port.

APPLICATION:
    A WSGI application import path. The format is the same that Gunicorn uses.
    Read more at <https://docs.gunicorn.org/en/stable/settings.html#wsgi-app>.
"""


def print_usage(file=sys.stdout) -> None:
    print(USAGE.format(name=sys.argv[0]), file=file, end="")


def die_with_usage(msg:str=None) -> NoReturn:
    if msg is not None:
        print(msg, file=sys.stderr)
    print_usage(sys.stderr)
    sys.exit(1)


def make_server(host: str, port: int, app: Any) -> Union[WSGIServer, WSGIServer6]:
    res = socket.getaddrinfo(
        host,
        port,
        type=socket.SOCK_STREAM,
        proto=socket.getprotobyname("tcp")
    )
    if any(e[0] is socket.AF_INET6 for e in res):
        family, _, _, _, sockaddr = next(e for e in res if e[0] is socket.AF_INET6)
    else:
        family, _, _, _, sockaddr = res[0]
    if family is socket.AF_INET:
        server_class = WSGIServer
    elif family is socket.AF_INET6:
        server_class = WSGIServer6
    else:
        raise ValueError("Unsupported family: {!s:s}".format(family))
    server = server_class(sockaddr, WSGIRequestHandler, bind_and_activate=False)
    server.set_app(app)
    try:
        server.server_bind()
        server.server_activate()
    except:
        server.server_close()
        raise
    return server


def main():
    if len(sys.argv) == 0:
        print_usage()
        sys.exit(0)
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "b:", ["bind"])
    except getopt.GetOptError as exc:
        die_with_usage(str(exc))
    if len(args) < 1:
        die_with_usage()
    app_uri = args[0]
    bind_address = None
    for option, value in optlist:
        if option in ("-b", "--bind"):
            bind_address = value
        else:
            assert False, "DEAD CODE"
    if bind_address is None:
        die_with_usage()
    host, port = parse_address(bind_address)
    app = import_app(app_uri)
    with make_server(host, port, app) as httpd:
        print("Listening on http://{:s}:{:d}/".format(("[" + host + "]") if is_ipv6(host) else host, port))
        httpd.serve_forever()
