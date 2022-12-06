"""
- rucksacks : List[rucksack]

- rucksack contains 2x compartment

- Rule no same item type spread in both comparment

- One item type per rucksack is missplaced and exists in both compartments

- Items of each rucksack on each line

- ALWAYS same number of items in each compartment

- proprity a-z == 1-26, A-Z == 27-52
"""

import string
from typing import Iterable
import itertools


# Read and format data =================================================================
# Read puzzle input and format data so we have list of lists (rucksacks of compartments)
with open("03/rucksacks.txt", 'r') as file:
    data = file.read().split('\n')

# make sure that all rows have even numbers
assert sum(len(rucksack) % 2 for rucksack in data) == 0

# Divide items into two compartments (list of lists)
rucksacks = []
for rucksack in data:
    num_items = len(rucksack) // 2
    rucksacks.append([rucksack[:num_items], rucksack[num_items:]])

# Create priority table ================================================================
item_to_priority = dict(zip(string.ascii_letters, range(1, 53)))


# Find equals ==========================================================================
# Find equal in rucksacks, assume only one item contains equal and priotiry i only per 
# item type, not number of items
def find_equal(x: Iterable, y: Iterable):
    for item in x:
        if item in y:
            return item

duplicated_types = [find_equal(*rucksack) for rucksack in rucksacks]

priorities = [item_to_priority[item_type] for item_type in duplicated_types]

# Print results of first rucksacks
for (c1, c2), item_type, prio in list(zip(rucksacks, duplicated_types, priorities))[:5]:
    print(f"{c1:<25} {c2:<25} {item_type} {prio}")

# Results
print("Total sum of priorities: ", sum(priorities))

# PART TWO =============================================================================

# Divide data into groups of three elves
def grouper(n: int, items: Iterable):
    """Create groups of 'n' items.

    Reference
    ---------
    https://stackoverflow.com/questions/2461484/idiomatic-way-to-take-groups-of-n-items-from-a-list-in-python
    """
    return itertools.zip_longest(*[iter(items)]*n)

groups = list(grouper(3, data))

def find_all_equals(*iterables: Iterable):
    """Find items that exists in all groups"""
    combinations = itertools.product(*iterables)
    for comb in combinations:
        if all(comb[0] == item for item in comb):
            yield comb[0]


# Lest assume as stated in task that groups only have one item type in common
badges = (next(find_all_equals(*group)) for group in groups)

total_badge_priority = sum(map(lambda x: item_to_priority[x], badges))

print("Total badge priority: ", total_badge_priority)