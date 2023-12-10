import re
from collections import defaultdict
from itertools import batched
from typing import Callable

import pyperclip

with open('input.txt') as f:
    data = f.read().strip()


class MultiRange:
    def __init__(self, c_val: list[int] | range):
        if isinstance(c_val, range):
            self.values = [c_val.start, c_val.stop]
            return
        assert len(c_val) % 2 == 0
        assert c_val == sorted(c_val)
        self.values = c_val

    @classmethod
    def _from_toggles(cls, a, b, cond):
        a = [(i, False) for i in a.values]
        b = [(i, True) for i in b.values]
        res = []
        active = [False, False]
        for x, s in sorted(a+b):
            a = cond(active)
            active[s] ^= 1
            if cond(active) != a:
                if res[-1:] == [x]:
                    res.pop()
                    continue
                res.append(x)
        return cls(res)

    def __or__(self, other):
        if not self.values: return other
        if not other.values: return self
        return MultiRange._from_toggles(self, other, any)

    def __and__(self, other):
        if not self.values or not other.values: return MultiRange([])
        return MultiRange._from_toggles(self, other, all)

    def __sub__(self, other):
        if not self.values: return MultiRange([])
        if not other.values: return self
        return MultiRange._from_toggles(self, other, lambda x: x[0] and not x[1])

    def __copy__(self):
        return MultiRange(self.values.copy())

    copy = __copy__

    def as_range_list(self) -> list[range]:
        return [range(a, a+b) for a, b in batched(self.values, 2)]

    def __repr__(self):
        return f"MultiRange({self.values})"


def try_int(s: str) -> int | str:
    try:
        return int(s)
    except ValueError:
        return s


SURROUND_DELTAS = [
    -1-1j, -1, -1+1j,
     0-1j,      0+1j,
     1-1j,  1,  1+1j,
]


def any_surround(pos: complex) -> list[complex]:
    return [pos + delta for delta in SURROUND_DELTAS]


class SparseGrid[T](defaultdict[complex, T]):
    def __init__(self, items: dict[complex, T] | None = None):
        super().__init__(lambda: None, items or {})

    @classmethod
    def from_input(cls, lines: list[str], converter: Callable[[str], T | None]):
        instance = cls()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if (converted := converter(char)) is None:
                    continue
                instance[y, x] = converted
        return instance

    def __getitem__(self, item):
        if isinstance(item, tuple):
            item = complex(*item)
        return super().__getitem__(item)

    def __setitem__(self, key: complex | tuple[int, int], value: T):
        if isinstance(key, tuple):
            key = complex(*key)
        return super().__setitem__(key, value)

    def __str__(self):
        contents = "; ".join(f"{int(k.real)},{int(k.imag)}:{v}" for k, v in self.items())
        return f"SparseGrid({contents})"

    def neighbor_pos(self, location: complex | tuple[int, int]) -> list[complex]:
        if isinstance(location, tuple):
            location = complex(*location)
        return [loc for loc in any_surround(location) if self[loc]]


class Grid[T]:
    def __init__(self, items: list[list[T]]):
        self.data = items
        self.h = len(items)
        self.w = len(items[0])

    @classmethod
    def from_input(cls, inp: list[str]):
        return Grid([list(map(try_int, line)) for line in inp])

    def _is_inbound(self, a, b):
        return 0 <= a < self.h and 0 <= b < self.w

    def __str__(self):
        if isinstance(self[0, 0], str):
            contents = [
                "  " + "".join(line)
                for line in self.data
            ]
        else:
            contents = [
                f"  [{" ".join(map(repr, row))}]"
                for row in self.data
            ]
        return "\n".join([
            "Grid([",
            *contents,
            "])"
        ])

    def __getitem__(self, item: complex | tuple[int, int]) -> T | None:
        if isinstance(item, complex):
            a = int(item.real)
            b = int(item.imag)
        elif isinstance(item, tuple):
            a, b = item
        else:
            raise IndexError(f"Invalid index type: {type(item)}")
        if not self._is_inbound(a, b):
            raise IndexError(f"Index out of bounds: ({a}, {b})")
        return self.data[a][b]

    def get_row(self, i: complex | int) -> list[T]:
        if isinstance(i, complex):
            i = int(i.real)
        return self.data[i].copy()

    def get_column(self, i: complex | int) -> list[T]:
        if isinstance(i, complex):
            i = int(i.imag)
        return [row[i] for row in self.data]

    def neighbor_index(self, location: complex | tuple[int, int]):
        if isinstance(location, tuple):
            location = complex(*location)
        return [
            loc
            for loc in any_surround(location)
            if self._is_inbound(int(loc.real), int(loc.imag))
        ]


def get_ints(s: str, allow_neg: bool = True) -> list[int]:
    r = [int(m) for m in re.findall("-?"*allow_neg + r"\d+", s)]
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
    import day09 as sol
    print(sol.res)
    pyperclip.copy(sol.res)

