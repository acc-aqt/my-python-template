""""""
from example_package.example_module import my_sum
from argparse import ArgumentParser


def entry_point():
    """An exemplary entry point. Takes two arguments and prints their sum."""

    parser = ArgumentParser(description="A simple CLI.")

    parser.add_argument("input_one", type=float)
    parser.add_argument("input_two", type=float)

    args = parser.parse_args()
    print(my_sum(args.input_one, args.input_two))
