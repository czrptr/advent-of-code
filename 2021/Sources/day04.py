from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

class Board:
  DIM = 5
  TRUES_ROW = np.array([True] * DIM)

  values: np.ndarray = None
  drawn: np.ndarray = None

  def isWinning(self) -> bool:
    for i in range(Board.DIM):
      row = self.drawn[i, :]
      col = self.drawn[:, i]

      if np.array_equal(row, Board.TRUES_ROW) \
        or np.array_equal(col, Board.TRUES_ROW):
        return True
    return False

  def loosing_sum(self) -> int:
    not_drawn = np.logical_not(self.drawn)
    return sum(self.values[not_drawn])

  def __init__(self, values: np.ndarray, drawn: np.ndarray):
    self.values = values
    self.drawn = drawn

  def __str__(self) -> str:
    return f"{self.values}\n{self.drawn}"

  def __repr__(self) -> str:
    return self.__str__()

NO_DRAWS = np.array([[False] * 5] * 5)

# ---------- Input ---------- #

numbers: T.List[int] = []
boards: T.List[Board] = []

lines: T.List[str] = []
with aoc.input() as file:
  lines = [line.strip() for line in file.readlines() if len(line.strip()) > 0]
  numbers = [int(number) for number in lines[0].split(",")]
  for i in range((len(lines) - 1) // 5):
    board: T.List[T.List[int]] = []
    for j in range(5):
      board.append([int(number) for number in re.split(r"\s+", lines[i * 5 + j + 1])])
    boards.append(Board(np.array(board), np.copy(NO_DRAWS)))

# ---------- Solution ---------- #

wins: T.List[T.Tuple[Board, int]] = []
while len(boards) > 0:
  drawn = numbers.pop(0)
  for board in boards:
    for (i, j) in matrix_indexes(Board.DIM, Board.DIM):
      if board.values[i, j] == drawn:
        board.drawn[i, j] = True

  current_winning_boards = list(filter(lambda b: b.isWinning(), boards))
  wins += zip(current_winning_boards, [drawn] * len(current_winning_boards))
  boards = list(filter(lambda b: not b.isWinning(), boards))

first_win = wins[0]

aoc.part1 = first_win[0].loosing_sum() * first_win[1]

last_win = wins[-1]

aoc.part2 = last_win[0].loosing_sum() * last_win[1]

aoc.print()
