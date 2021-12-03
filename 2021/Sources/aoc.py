from __future__ import annotations
import typing as T
import itertools as iter
import more_itertools as iter
import functools as func
import numpy as np

import enum
import sys
import os
import re

class aoc:
  part1 = None
  part2 = None
  __day = None

  @staticmethod
  def init(file_path: str):
    file_name = os.path.basename(file_path)
    assert re.match(r"day\d+", file_name)
    aoc.__day = file_name[3:-3] # (Day).*(.py)

  @staticmethod
  def input():
    return open(f"../Resources/input{aoc.__day}.txt", "r")

  @staticmethod
  def print():
    print(f"Day {aoc.__day}")
    print(f"├─Part 01: {aoc.part1}")
    print(f"└─Part 02: {aoc.part2}")

# ---------- Utils ---------- #

def unreachable():
  assert False, "unreachable"

@enum.unique
class Comparison(enum.IntEnum):
  LESSER = enum.auto()
  EQUAL = enum.auto()
  GREATER = enum.auto()

def compare(a: int, b: int) -> Comparison:
  if a < b: return Comparison.LESSER
  if a == b: return Comparison.EQUAL
  return Comparison.GREATER