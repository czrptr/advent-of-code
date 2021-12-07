from __future__ import annotations
import typing as T

from functools import *

def negation(f: T.Callable) -> T.Callable:
  return lambda *args, **kargs: not f(*args, **kargs)

def identity(arg):
  return arg
