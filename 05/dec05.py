


import itertools
from typing import Iterable
import string


with open("05/procedure.txt") as file:
    data = file.read().splitlines()

data_stacks = data[:9]
data_moves = data[10:]

def get_stacks(raw_stacks: list[str]):
    # get stack numbers
    data_stacks = raw_stacks.copy()
    stack_numbers = data_stacks.pop()
    stack_numbers: list[str] = stack_numbers.split(' ')
    stack_numbers = [int(number) for number in stack_numbers if number.isnumeric()]

    # Instantiate empty stacks
    stacks: dict[int, list[str]] = {number: [] for number in stack_numbers}

    # Clean stacks
    data_stacks = [stack.replace('[', ' ').replace(']', ' ') for stack in data_stacks]

    # Split stacks
    data_stacks = list(zip(*data_stacks))

    # Remove 'stacks' that not contain any characters
    cleaned_stacks = []
    for stack in data_stacks:
        if any(c in string.ascii_uppercase for c in stack):
            cleaned_stacks.append([c for c in stack if c in string.ascii_uppercase])
    for stack in cleaned_stacks:
        stack.reverse() 

    # Populate stacks
    stacks = {num: stack for num, stack in enumerate(cleaned_stacks, start=1)}
    return stacks

def print_stacks(stacks: dict[int, list]) -> None:
    s = list(itertools.zip_longest(*stacks.values(), fillvalue=' '))
    s.reverse() # Reverse for printing
    for row in s:
        print(*row)
    print('_'*(len(s)*2+1))
    print(*stacks.keys())

def parse_move(line: str) -> tuple[int, int, int]:
    words: list[str] = line.split(' ')
    return tuple(int(word) for word in words if word.isnumeric())

assert parse_move("move 13 from 3 to 2") == (13, 3, 2)

def move(num: int, source_stack: list, dest_stack: list) -> None:
    for _ in range(num):
        crate = source_stack.pop()
        dest_stack.append(crate)


# Process movements
# print(stacks)

stacks = get_stacks(data_stacks)
print_stacks(stacks)
for num, movement_raw in enumerate(data_moves):
    num, source, dest = parse_move(movement_raw)
    move(num, stacks[source], stacks[dest])

def get_top_crates_of(stacks: dict) -> str:
    return ''.join([stack[-1] for stack in stacks.values() if stack])

print_stacks(stacks)
print("Top containers: ", get_top_crates_of(stacks))



# PART TWO ==== 
def move_multiple(num: int, source_stack: list, dest_stack: list) -> None:
    creates = [source_stack.pop() for _ in range(num)]
    creates.reverse()
    dest_stack += creates

stacks = get_stacks(data_stacks)
print_stacks(stacks)
for num, movement_raw in enumerate(data_moves):
    num, source, dest = parse_move(movement_raw)
    move_multiple(num, stacks[source], stacks[dest])

def get_top_crates_of(stacks: dict) -> str:
    return ''.join([stack[-1] for stack in stacks.values() if stack])

print_stacks(stacks)
print("Top containers 9001: ", get_top_crates_of(stacks))