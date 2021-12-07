from aoc import *

TEMPLATE = """
from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

# ---------- Input ---------- #

with aoc.input() as file:
  pass

# ---------- Solution ---------- #

aoc.print()
""".strip()

CWD = os.getcwd()

def error(msg: str) -> T.NoReturn:
  print(f"Create AoC solution: {msg}")
  exit()

def validate(args: T.List[str]) -> T.Tuple[str, str]:
  # length validated in task
  year, day = args[1:3]

  if not year.isnumeric():
    error("year needs to be a number")

  year = int(year)
  if not year >= 2015:
    error("year need to be 2015 or later")

  if not day.isnumeric():
    error("day needs to be a number")

  day = int(day)
  if not 1 <= day <= 25:
    error("day need to be between 1 and 25")

  return (year, day)

def main(args: T.List[str]):
  year, day = validate(args)

  resources = f"{CWD}/{year}/Resources"
  os.makedirs(resources, exist_ok = True)
  open(f"{resources}/input{day:02}.txt", "w").close()

  sources = f"{CWD}/{year}/Sources"
  os.makedirs(sources, exist_ok = True)
  with open(f"{sources}/day{day:02}.py", "w") as file:
    file.write(TEMPLATE)

if __name__ == "__main__":
  main(sys.argv)
else:
  assert False