"""This module provides the RP Tree CLI"""
# cli.py

import argparse
import pathlib
import sys

from . import __version__


def parse_cmd_line_arguments():
    parse = argparse.ArgumentParser(
        prog="tree",
        description="RP Tree, a directory tree generator",
        epilog="Thanks for using RP Tree"
    )
    parse.version = f"RP Tree v{__version__}"
    parse.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generate a full directory tree and save it to a file"
    )
    parse.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory only tree"
    )
    parse.add_argument("-v", "--version", action="version")
    parse.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR"
    )
    return parse.parse_args()
