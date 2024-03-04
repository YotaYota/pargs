import argparse

from pargs import __version__
from pargs.util.foo_helper import return_baz, return_foo


def create_parser():
    parser = argparse.ArgumentParser(description="PArgs CLI")
    parser.add_argument("-f", "--foo",
                        help="Foo")
    parser.add_argument("-b", "--baz",
                        help="Baz")
    parser.add_argument("-V", "--version", action="version",
                        version=__version__,
                        help="Print version and exit")
    return parser


def handle_args(args):
    if args.foo:
        print(f"Foo was called with {args.foo}")
        print(f"foo-helper returns {return_foo()}")
    if args.baz:
        print(f"Baz was called with {args.baz}")
        print(f"baz-helper returns {return_baz()}")


def cli(*args, **kwargs):
    print(*args)
    print(**kwargs)
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)
