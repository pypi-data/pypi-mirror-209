import getopt
from wsgiref.simple_server import make_server
from typing import NoReturn
import sys
from .load_wsgiapp import import_app


USAGE: str = """\
Usage: {name!s:s} [-b ADDRESS | --bind ADDRESS] APPLICATION

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
    parts = bind_address.rsplit(":", 1)
    if len(parts) != 2:
        die_with_usage("Malformed ADDRESS")
    host, port = parts
    try:
        port = int(port)
    except ValueError:
        die_with_usage("Malformed PORT in ADDRESS")
    app = import_app(app_uri)
    with make_server(host, port, app) as httpd:
        httpd.serve_forever()
