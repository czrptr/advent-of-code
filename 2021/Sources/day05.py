from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __eq__(self, other) -> bool:
    return self.x == other.x and self.y == other.y

  def __str__(self) -> str:
    return f"({self.x}, {self.y})"

  def __repr__(self) -> str:
    return self.__str__()

class Line:
  def __init__(self, a: Point, b: Point):
    self.a = a
    self.b = b

  def is_aa(self) -> bool:
    return self.a.x == self.b.x or self.a.y == self.b.y

  def __str__(self) -> str:
    return f"({self.a}, {self.b})"

  def __repr__(self) -> str:
    return self.__str__()

# ---------- Input ---------- #

lines: T.List[Line] = []
W, H = 0, 0

with aoc.input() as file:
  str_points = [line.strip().split(" -> ") for line in file.readlines()]
  for str_a, str_b in str_points:
    a = [int(coord) for coord in str_a.split(",")]
    b = [int(coord) for coord in str_b.split(",")]
    W = max(W, a[0], b[0])
    H = max(H, a[1], b[1])
    lines.append(Line(Point(a[0], a[1]), Point(b[0], b[1])))

W += 1
H += 1

# ---------- Solution ---------- #

diagram = np.array([[0] * W] * H) #[y, x]

for l in filter(Line.is_aa, lines):
  if l.a.x == l.b.x:
    x = l.a.x
    y1, y2 = (l.a.y, l.b.y) if l.a.y < l.b.y else (l.b.y, l.a.y)
    diagram[y1 : y2 + 1, x] += 1
  else: # l.a.y == l.b.y
    y = l.a.y
    x1, x2 = (l.a.x, l.b.x) if l.a.x < l.b.x else (l.b.x, l.a.x)
    diagram[y, x1 : x2 + 1] += 1

aoc.part1 = np.count_nonzero(diagram >= 2)

for l in filter(func.negation(Line.is_aa), lines):
  p = l.a
  while p != l.b:
    diagram[p.y, p.x] += 1
    p.x += clamp(l.b.x - p.x, -1, 1)
    p.y += clamp(l.b.y - p.y, -1, 1)
  diagram[p.y, p.x] += 1

aoc.part2 = np.count_nonzero(diagram >= 2)

aoc.print()