from __future__ import annotations
import typing as T
import itertools as iter
import more_itertools as iter

# example
# measurements = [
#   199, 200, 208, 210, 200,
#   207, 240, 269, 260, 263,
# ]

measurements: T.List[int] = []
with open("../Resources/day1input.txt", "r") as file:
  measurements = [int(line.strip()) for line in file.readlines()]

# part 1

increases = 0
for a, b in iter.pairwise(measurements):
  if a < b:
    increases += 1

print(increases)

# part 2

increases = 0
for t1, t2 in iter.pairwise(iter.windowed(measurements, 3)):
  if sum(t1) < sum(t2):
    increases += 1

print(increases)
