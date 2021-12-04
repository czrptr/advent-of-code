from aoc import *
aoc.init(__file__)

# ---------- Setup ---------- #

def intFromBase2(bits: T.List[int]) -> int:
  return int(''.join([str(bit) for bit in bits]), 2)

def bitNegation(bits: T.List[int]) -> T.List[int]:
  return [int(bool(bit - 1)) for bit in bits]

def most_common(bits: T.Iterator[int]) -> int:
  return (0, 1)[list(bits).count(1) >= list(bits).count(0)]

def bit_filter(report: np.ndarray, bias: int) -> T.List[int]:
  aux = []
  for col in range(W):
    if np.shape(report)[0] == 1:
      break

    bias_bit = abs(1 - bias - most_common(report[:, col]))
    for row in range(np.shape(report)[0]):
      if report[row, col] == bias_bit:
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