from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

def sumTo(n: int) -> int:
  return n * (n + 1) // 2

def min_cost(crabs: T.List[int], dist: T.Callable) -> int:
  cost = math.inf
  for pos in range(min(crabs), max(crabs) + 1):
    current_cost = sum(dist(abs(c - pos)) for c in crabs)
    cost = min(cost, current_cost)

  return cost

# ---------- Input ---------- #

crabs: T.List[int] = []
with aoc.input() as file:
  crabs = [int(n) for n in file.readline().split(",")]

# ---------- Solution ---------- #

aoc.part1 = min_cost(crabs, func.identity)

aoc.part2 = min_cost(crabs, lambda a: sumTo(a))

aoc.print()
