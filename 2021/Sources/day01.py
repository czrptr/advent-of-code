from aoc import *
aoc.init(__file__)

# ---------- Input ---------- #

measurements: T.List[int] = []
with aoc.input() as file:
  measurements = [int(line.strip()) for line in file.readlines()]

# ---------- Solution ---------- #

aoc.part1 = sum(int(a < b) for a, b in iter.pairwise(measurements))

aoc.part2 = sum(int(sum(t1) < sum(t2)) for t1, t2 in iter.pairwise(iter.windowed(measurements, 3)))

aoc.print()
