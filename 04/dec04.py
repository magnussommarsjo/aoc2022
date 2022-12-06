
from __future__ import annotations
# Read and transform data

from dataclasses import dataclass
from typing import List


with open("04/section_assignments.txt") as file:
    data = file.read().splitlines()

# Lets create a class for this

@dataclass
class Assignment:
    start: int
    stop: int

    def contains(self, other: Assignment) -> bool:
        if (self.start <= other.start) and (self.stop >= other.stop):
            return True
        else:
            return False
    
    # USED FOR PART TWO
    def overlap(self, other: Assignment) -> bool:
        if (self.start <= other.stop) and (self.stop >= other.start):
            return True
        else:
            return False

# Create pairs of Assignment
#
# [
#   [...],
#   [['num', 'num'], ['num', 'num']],
#   [...], 
# ]
#
#


def format_raw_assignment(raw: str) -> list[int, int]:
    items = raw.split('-')
    return [int(item) for item in items]

pairs: list[list[Assignment, Assignment]] = []
for line in data:
    elfs = line.split(',')
    pairs.append([Assignment(*format_raw_assignment(elf)) for elf in elfs])

fully_contains: list[bool] = []
for pair in pairs:
    fully_contains.append(pair[0].contains(pair[1]) or pair[1].contains(pair[0]))

# Check logic
for pair, contains in list(zip(pairs, fully_contains))[:5]:
    print(pair, contains)

print("Total fully contained pairs: ", sum(fully_contains))


# PART TWO ============================================================================
assert Assignment(1, 5).overlap(Assignment(4, 10))
assert not Assignment(1, 5).overlap(Assignment(6, 10))


overlaps = [pair[0].overlap(pair[1]) for pair in pairs]

# Check logic
for pair, overlap in list(zip(pairs, overlaps))[:20]:
    print(pair, overlap)

print("Total fully overlaped pairs: ", sum(overlaps))
