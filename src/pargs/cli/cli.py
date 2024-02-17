import argparse

from pargs import __version__


def create_parser():
    parser = argparse.ArgumentParser(description="PArgs CLI")
    parser.add_argument("-f", "--foo",
                        help="Foo")
    parser.add_argument("-V", "--version", action="version",
                        version=__version__,
                        help="Print version and exit")
    return parser


def handle_args(args):
    if args.foo:
        print(f"Foo was called with {args.foo}")


def main_cli(*args, **kwargs):
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)
