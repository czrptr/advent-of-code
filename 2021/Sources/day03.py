from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

def intFromBase2(bits: T.List[int], bits_reversed: bool = True) -> int:
  result = 0
  for exp, bit in enumerate(reversed(bits) if bits_reversed else bits):
    result += bit * pow(2, exp)
  return result

def bitNegation(bits: T.List[int]) -> T.List[int]:
  return [int(bool(bit - 1)) for bit in bits]

def most_common(bits: T.Iterator[int]) -> int:
  match compare(list(bits).count(0), list(bits).count(1)):
    case Comparison.LESSER | Comparison.EQUAL:
      return 1
    case Comparison.GREATER:
      return 0

def least_common(bits: T.Iterator[int]) -> int:
  match compare(list(bits).count(0), list(bits).count(1)):
    case Comparison.LESSER | Comparison.EQUAL:
      return 0
    case Comparison.GREATER:
      return 1

def bit_filter(report: np.ndarray, bias: int) -> T.List[int]:
  aux = []
  for col in range(W):
    if np.shape(report)[0] == 1:
      break

    common_bit = most_common(report[:, col]) if bias == 1 else least_common(report[:, col])
    for row in range(np.shape(report)[0]):
      if report[row, col] == common_bit:
        aux.append(list(report[row]))

    report, aux = np.array(aux), []

  return list(report[0])

# ---------- Input ---------- #

report_data: T.List[T.List[int]] = []
with aoc.input() as file:
  for line in file.readlines():
    report_data.append([int(char) for char in line.strip()])

report = np.array(report_data)
W = np.shape(report)[1]

# ---------- Solution ---------- #

gamma_bits = [most_common(report[:, col]) for col in range(W)]

aoc.part1 = intFromBase2(gamma_bits) * intFromBase2(bitNegation(gamma_bits))

generator_rating_bits = bit_filter(report, 1)
scrubber_rating_bits = bit_filter(report, 0)

aoc.part2 = intFromBase2(generator_rating_bits) * intFromBase2(scrubber_rating_bits)

aoc.print()