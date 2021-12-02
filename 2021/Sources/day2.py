from __future__ import annotations
import typing as T
import enum

@enum.unique
class Direction(enum.Enum):
  FORWARD = "forward"
  DOWN = "down"
  UP = "up"

Command = T.Tuple[Direction, int]

# example
# course: T.List[Command] = [
#   (Direction.FORWARD, 5),
#   (Direction.DOWN, 5),
#   (Direction.FORWARD, 8),
#   (Direction.UP, 3),
#   (Direction.DOWN, 8),
#   (Direction.FORWARD, 2),
# ]

course: T.List[Command] = []
with open("../Resources/day2input.txt", "r") as file:
  for line in file.readlines():
    dir_str, dist_str = line.strip().split(" ")
    course.append((Direction(dir_str), int(dist_str)))

# part 1

hpos, depth = (0,) * 2
for (dir, dist) in course:
  match dir:
    case Direction.FORWARD:
      hpos += dist
    case Direction.DOWN:
      depth += dist
    case Direction.UP:
      depth -= dist

print(hpos * depth)

# part 2

hpos, depth, aim = (0,) * 3
for (dir, dist) in course:
  match dir:
    case Direction.FORWARD:
      hpos += dist
      depth += aim * dist
    case Direction.DOWN:
      aim += dist
    case Direction.UP:
      aim -= dist

print(hpos * depth)