from __future__ import annotations
from dataclasses import dataclass

from typing import Optional


with open("07/terminal.txt", "r") as file:
    rows = file.read().splitlines()


class Directory:
    def __init__(self, name: str, parent_dir: Optional[Directory]) -> None:
        self.name = name
        self.parent_dir = parent_dir
        self.sub_dirs: list[Directory] = []
        self.files: list[File] = []
        self.total_size: Optional[int] = None

    def add_subdir(self, name: str) -> None:
        self.sub_dirs.append(Directory(name=name, parent_dir=self))
    
    def add_file(self, file: File) -> None:
        self.files.append(file)
    
    def get_total_files_size(self) -> int:
        return sum(file.size for file in self.files)
    
    def get_total_size(self) -> int:
        if self.total_size is not None:
            return total_size

        total_size = 0
        total_size += self.get_total_files_size()

        for dir in self.sub_dirs:
            total_size += dir.get_total_size()
        
        self.total_size = total_size
        return total_size
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"


@dataclass
class File:
    size: int
    name: str

root_dir = Directory(name= '/', parent_dir=None)
present_dir: Directory = root_dir # Assume start at root

def cd(arg: str):
    global present_dir
    if arg == '/':  # Go to root
        present_dir = root_dir
    elif arg == '..': # Go to parent
        if present_dir.name == '/':
            present_dir = root_dir
        else:
            present_dir = present_dir.parent_dir
    else:
        # Find correct dir of subdirectories
        for dir in present_dir.sub_dirs:
            if dir.name == arg:
                present_dir = dir
                return
        raise NotADirectoryError(f"Directory {arg} is not a subdirectory of {present_dir}")


def ls():
    # I guess we can just pass here
    pass

def process_command(parts: list):
    if parts[1] == 'cd':
        cd(parts[2])
    elif parts[1] == 'ls':
        ls()
    else:
        raise LookupError(f"Command {parts[1]} does not exist")


# Create directory tree
for idx, row in enumerate(rows):
    parts = row.split(' ')
    try:
        if parts[0] == '$':  # is a Command
            process_command(parts)
        elif parts[0] == 'dir':  # is a Directory
            present_dir.add_subdir(name=parts[1])
        else:  # Has to be a File
            present_dir.add_file(File(size=int(parts[0]), name=parts[1]))
    except Exception as e:
        print(f"row: {idx+1}")
        raise e



def get_list_directories(dir: Directory) -> list[Directory]:
    directories = []
    directories += dir.sub_dirs
    for sub_dir in dir.sub_dirs:
        directories += get_list_directories(sub_dir)
    
    return directories


directories = get_list_directories(root_dir)

print(len(directories))


total_size = root_dir.get_total_size()

sub_100_000 = [dir for dir in directories if dir.total_size <= 100_000]
print(f"count of dir below 100_000: {len(sub_100_000)}")
print(f"Total size: {sum([dir.total_size for dir in sub_100_000])}")


# PART TWO ==============================================
filesystem_size = 70_000_000
required_free_space = 30_000_000

present_space = filesystem_size - total_size
min_space_to_free_up = required_free_space - present_space

print(f"{min_space_to_free_up:_}")
directories.sort(key=lambda x: x.total_size)

# Print first directory that is above required size
for dir in directories:
    if dir.total_size >= min_space_to_free_up:
        print(dir.name, dir.total_size)
        break