import re
from typing import Callable

import pyperclip

with open('input.txt') as f:
    data = f.read().strip()


def try_int(s: str) -> int | str:
    try:
        return int(s)
    except ValueError:
        return s


def get_ints(s: str) -> list[int]:
    r = [int(m) for m in re.findall(r"\d+", s)]
    return r


def get_floats(s: str, allow_neg: bool = True) -> list[float]:
    return [float(m) for m in re.findall("-?"*allow_neg + r"\d+\.\d+", s)]


def grid(inp: list[str], keep: Callable[[str], bool], convert_digits: bool = True) -> dict[complex, str | int]:
    res = {}
    for y, line in inp:
        for x, char in line:
            if not keep(char):
                continue
            res[complex(x, y)] = try_int(char) if convert_digits else char
    return res


if __name__ == '__main__':
    import day03 as sol
    print(sol.res)
    pyperclip.copy(sol.res)

