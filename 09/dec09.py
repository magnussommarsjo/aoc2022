from __future__ import annotations

from dataclasses import dataclass
import enum
import itertools
from typing import Optional

def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(value, high))


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: Position) -> Position:
        return Position(
            x = self.x + other.x,
            y = self.y + other.y
        )
    
    def __sub__(self, other: Position) -> Position:
        return Position(
            x = self.x - other.x,
            y = self.y - other.y
        )
    
    def clamp(self, low: int, high: int) -> Position:
        return Position(clamp(self.x, low, high), clamp(self.y, low, high))


# Test pos
assert len({Position(1,1), Position(1,1), Position(1,2)}) == 2
assert Position(1,1) == Position(1,1)  # Equality
assert Position(1,1) == Position(2,2).clamp(-1, 1) # Clamp pos
assert Position(-1, -1) == Position(-2, -2).clamp(-1, 1)   # Clamp neg

class Direction(str, enum.Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"

def move(position: Position, direction: Direction) -> Position:
    match direction:
        case Direction.UP:
            position = position + Position(0,1)
        case Direction.RIGHT:
            position = position + Position(1,0)
        case Direction.DOWN:
            position = position - Position(0,1)
        case Direction.LEFT:
            position = position - Position(1,0)
        
    return position

class Knot:
    def __init__(self):
        self.leading_knot: Optional[Knot] =  None
        self.trailing_knot: Optional[Knot] = None
        self.pos = Position(0,0)
        self.history: list[Position] = [Position(0,0)]
    
    def follow(self):
        if self.leading_knot is None:
            # Nothing to follow
            return

        if self.pos == self.leading_knot.pos:
            # Head is covering tail. Do nothing
            return
        
        offset = self.leading_knot.pos - self.pos
        if abs(offset.x) > 1 or abs(offset.y) > 1:
            # Distance too large. Tail needs to move. 
            self.pos = self.pos + offset.clamp(-1, 1)
            # Log new position
            self.history.append(self.pos)
        
        if self.trailing_knot is not None:
            self.trailing_knot.follow()

class Rope:
    def __init__(self, num_knots: int):
        self.knots: list[Knot] = [Knot() for _ in range(num_knots)]
        self.head_knot = self.knots[0]

        # Connect knots
        for idx, knot in enumerate(self.knots):
            if idx == 0:
                # First knot
                continue
            else:
                leading_knot = self.knots[idx-1]
                leading_knot.trailing_knot = knot
                knot.leading_knot=leading_knot
                
    
    def move_head(self, direction: Direction, distance: int) -> None:
        for _ in range(distance):
            self.head_knot.pos = move(self.head_knot.pos, direction)
            self.head_knot.trailing_knot.follow()
        
    




def read_input(row: str) -> tuple[Direction, int]:
    raw_direction, raw_distance = row.split(' ')
    distance = int(raw_distance)
    match raw_direction:
        case Direction.UP:
            return Direction.UP, distance
        case Direction.DOWN:
            return Direction.DOWN, distance
        case Direction.LEFT:
            return Direction.LEFT, distance
        case Direction.RIGHT:
            return Direction.RIGHT, distance


# PART ONE ====================

rope = Rope(num_knots=2)

with open("09/moves.txt", 'r') as file:
    data = file.read().splitlines()

for row in data:
    direction, distance = read_input(row)
    rope.move_head(direction, distance)


print("Number of unique positions of tail: ", len(set(rope.knots[-1].history)))

# PART TWO
rope = Rope(10)

for row in data:
    direction, distance = read_input(row)
    rope.move_head(direction, distance)

# Combining history lists together, then flatten them through iterations into set

tail_history = set(rope.knots[-1].history)

print("Number of unique positions of long tail: ", len(tail_history))

