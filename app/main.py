# !/usr/bin/env python3
# tree.py

"""This module provides RP Tree entry point script"""
import sys
import pathlib
from app.cli import parse_cmd_line_arguments
from app.gen_tree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doen't exist")
        sys.exit()
    tree = DirectoryTree(root_dir, dir_only=args.dir_only,
                         output_file=args.output_file,levels=args.levels)
    tree.generate()


if __name__ == "__main__":
    main()
