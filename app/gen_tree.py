# rptree.py

"""This module provides RP Tree main module."""
import os
import pathlib
import sys

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

exclude_list = [".git","__pycache__"]

class DirectoryTree:
    def __init__(self, root_dir, dir_only=False, output_file=sys.stdout, levels=999):
        self._output_file = output_file
        self._generator = _TreeGenerator(root_dir, dir_only, levels )

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)
        if self._output_file != sys.stdout:
            # Wrap the tree in a markdown code
            tree.insert(0, "```")
            tree.append("```")
            self._output_file = open(
                self._output_file, mode="w", encoding="UTF-8"
            )
            with self._output_file as stream:
                for entry in tree:
                    print(entry, file=stream)


class _TreeGenerator:
    def __init__(self, root_dir, dir_only=False, levels=999):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        self._tree = []
        self.levels = levels
        self.level = 0

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        if not self._dir_only:
            self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        self.level = self.level + 1
        entries = self._prepare_entries(directory)
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            if not entry.name in exclude_list:
                connector = ELBOW if index == entries_count - 1 else TEE
                if entry.is_dir():
                    if self.level < self.levels:
                        self._add_directory(
                            entry, index, entries_count, prefix, connector
                        )
                    else:
                        self._add_file( entry, prefix, connector )
                else:
                    self._add_file(entry, prefix, connector)
        self.level = self.level - 1

    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries

    def _add_directory(
        self, directory, index, entries_count, prefix, connector
    ):
        self._tree.append(f"{prefix}{connector}{directory.name}{os.sep}")
        if index != entries_count-1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(
            directory=directory,
            prefix=prefix
        )
        if not self._dir_only:
            self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        postfix = ""
        if file.is_dir():
            postfix = os.sep
        self._tree.append(f"{prefix}{connector}{file.name}{postfix}")
