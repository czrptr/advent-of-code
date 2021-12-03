from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

@enum.unique
class Direction(enum.Enum):
  FORWARD = "forward"
  DOWN = "down"
  UP = "up"

Command = T.Tuple[Direction, int]

# ---------- Input ---------- #

course: T.List[Command] = []
with aoc.input() as file:
  for line in file.readlines():
    dir_str, dist_str = line.strip().split(" ")
    course.append((Direction(dir_str), int(dist_str)))

# ---------- Solution ---------- #

hpos, depth = (0,) * 2
for (dir, dist) in course:
  match dir:
    case Direction.FORWARD:
      hpos += dist
    case Direction.DOWN:
      depth += dist
    case Direction.UP:
      depth -= dist

aoc.part1 = hpos * depth

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

aoc.part2 = hpos * depth

aoc.print()