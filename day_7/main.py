import itertools
import re

PATTERN_DIR = re.compile(r"dir (.+)")
PATTERN_FILE = re.compile(r"(\d+) (.+)")
PATTERN_COMMAND_UP = re.compile(r"\$ cd \.\.")
PATTERN_COMMAND_ROOT = re.compile(r"\$ cd /")
PATTERN_COMMAND_CD = re.compile(r"\$ cd (.+)")
PATTERN_COMMAND_LIST = re.compile(r"\$ ls")

DIR = "DIR"
FILE = "FILE"
UP = "UP"
ROOT = "ROOT"
CD = "CD"
LST = "LST"


def indent(string, indentation=' '):
    return '\n'.join([indentation + st for st in string.split('\n')])


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.set_parent(parent)
        self._size = 0
        self._files = []
        self._dirs = {}

    def add_size(self, size):
        self._size += size

        if self._parent:
            self._parent.add_size(size)

    def get_size(self):
        return self._size

    def add_file(self, name, size):
        self._files.append(name)
        self.add_size(size)

    def set_parent(self, parent):
        self._parent = parent

    def add_dir(self, name):
        dir = Dir(name, parent=self)
        self._dirs[name] = dir
        return dir

    def get_parent(self):
        return self._parent

    def get_child(self, name):
        return self._dirs[name]

    def get_children(self):
        return list(self._dirs.values())


def flatten_tree(root):
    return [root] + list(itertools.chain(*[flatten_tree(child) for child in root.get_children()]))


def interpret_line(line):
    dir_match = PATTERN_DIR.match(line)
    file_match = PATTERN_FILE.match(line)
    up_match = PATTERN_COMMAND_UP.match(line)
    root_match = PATTERN_COMMAND_ROOT.match(line)
    cd_match = PATTERN_COMMAND_CD.match(line)
    list_match = PATTERN_COMMAND_LIST.match(line)

    if dir_match:
        name = dir_match.groups()[0]
        return DIR, name

    if file_match:
        size, name = file_match.groups()
        return FILE, name, int(size)

    if up_match:
        return (UP,)

    if root_match:
        return (ROOT,)

    if cd_match:
        name = cd_match.groups()[0]
        return (CD, name)

    if list_match:
        return (LST,)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    root_dir = Dir("root")
    current_dir = root_dir

    for line in input_lines:
        command = interpret_line(line)
        action = command[0]

        if action == ROOT:
            current_dir = root_dir

        if action == UP:
            current_dir = current_dir.get_parent()

        if action == CD:
            current_dir = current_dir.get_child(command[1])

        if action == FILE:
            current_dir.add_file(*command[1:])

        if action == DIR:
            current_dir.add_dir(command[1])

    dir_list = flatten_tree(root_dir)
    sizes = [directory.get_size() for directory in dir_list]
    part_1 = sum([size for size in sizes if size <= 100000])
    print("part 1: ", part_1)

    total = 70000000
    needed = 30000000
    used = root_dir.get_size()
    free = total - used
    to_free = needed - free
    sizes.sort()
    print("part 2: ", next(itertools.dropwhile(lambda x: x < to_free, sizes)))
