from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

OLD_SPAWN = 6
NEW_SPAWN = 8

def simulate_days(fish: T.Mapping[int, int], days: int) -> T.Mapping[int, int]:
  for _ in range(days):
    spawned = fish[0]
    for i in range(NEW_SPAWN):
      fish[i] = fish[i + 1]
    fish[OLD_SPAWN] += spawned
    fish[NEW_SPAWN] = spawned
  return fish

# ---------- Input ---------- #

fish: T.Mapping[int, int] = {}
with aoc.input() as file:
  nums = [int(n) for n in file.readline().split(",")]
  for i in range(NEW_SPAWN + 1):
    fish[i] = nums.count(i)

# ---------- Solution ---------- #

fish = simulate_days(fish, 80)

aoc.part1 = sum(fish.values())

fish = simulate_days(fish, 256 - 80)

aoc.part2 = sum(fish.values())

aoc.print()
