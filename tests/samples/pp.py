from __future__ import division


@snoop(depth=30)
def main():
    x = 1
    y = 2
    pp(pp(x + 1) + max(*pp(y + 2, y + 3)))
    assert pp.deep(lambda: x + 1 + max(y + 2, y + 3)) == 7
    lst = list(range(30))
    pp.deep(lambda: list(
        list(a + b for a in [1, 2])
        for b in [3, 4]
    ) + lst)
    pp(dict.fromkeys(range(30), 4))
    pp.deep(lambda: BadRepr() and 1)
    pp.deep(lambda: 1 / 2)

    try:
        pp.deep(lambda: max(y + 2, (y + 3) / 0))
    except ZeroDivisionError:
        pass
    else:
        assert 0


class BadRepr(object):
    def __repr__(self):
        raise ValueError('bad')


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 5
12:34:56.78    5 | def main():
12:34:56.78    6 |     x = 1
12:34:56.78    7 |     y = 2
12:34:56.78    8 |     pp(pp(x + 1) + max(*pp(y + 2, y + 3)))
12:34:56.78 LOG:
12:34:56.78 .... x + 1 = 2
12:34:56.78 LOG:
12:34:56.78 .... y + 2 = 4
12:34:56.78 .... y + 3 = 5
12:34:56.78 LOG:
12:34:56.78 .... pp(x + 1) + max(*pp(y + 2, y + 3)) = 7
12:34:56.78    9 |     assert pp.deep(lambda: x + 1 + max(y + 2, y + 3)) == 7
12:34:56.78 LOG:
12:34:56.78 ............ x = 1
12:34:56.78 ........ x + 1 = 2
12:34:56.78 ................ y = 2
12:34:56.78 ............ y + 2 = 4
12:34:56.78 ................ y = 2
12:34:56.78 ............ y + 3 = 5
12:34:56.78 ........ max(y + 2, y + 3) = 5
12:34:56.78 .... x + 1 + max(y + 2, y + 3) = 7
12:34:56.78   10 |     lst = list(range(30))
12:34:56.78 .......... lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ..., 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
12:34:56.78 .......... len(lst) = 30
12:34:56.78   11 |     pp.deep(lambda: list(
12:34:56.78 LOG:
12:34:56.78 ............ list(a + b for a in [1, 2])
12:34:56.78              for b in [3, 4] = <generator object <genexpr> at 0xABC>
12:34:56.78 .................... a + b for a in [1, 2] = <generator object <genexpr> at 0xABC>
12:34:56.78 ............................ a = 1
12:34:56.78 ............................ b = 3
12:34:56.78 ........................ a + b = 4
12:34:56.78 ............................ a = 2
12:34:56.78 ............................ b = 3
12:34:56.78 ........................ a + b = 5
12:34:56.78 ................ list(a + b for a in [1, 2]) = [4, 5]
12:34:56.78 .................... a + b for a in [1, 2] = <generator object <genexpr> at 0xABC>
12:34:56.78 ............................ a = 1
12:34:56.78 ............................ b = 4
12:34:56.78 ........................ a + b = 5
12:34:56.78 ............................ a = 2
12:34:56.78 ............................ b = 4
12:34:56.78 ........................ a + b = 6
12:34:56.78 ................ list(a + b for a in [1, 2]) = [5, 6]
12:34:56.78 ........                 list(
12:34:56.78              list(a + b for a in [1, 2])
12:34:56.78              for b in [3, 4]
12:34:56.78          ) = [[4, 5], [5, 6]]
12:34:56.78 ........ lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
12:34:56.78 ....                 list(
12:34:56.78          list(a + b for a in [1, 2])
12:34:56.78          for b in [3, 4]
12:34:56.78      ) + lst = [[4, 5],
12:34:56.78                 [5, 6],
12:34:56.78                 0,
12:34:56.78                 1,
12:34:56.78                 2,
12:34:56.78                 3,
12:34:56.78                 4,
12:34:56.78                 5,
12:34:56.78                 6,
12:34:56.78                 7,
12:34:56.78                 8,
12:34:56.78                 9,
12:34:56.78                 10,
12:34:56.78                 11,
12:34:56.78                 12,
12:34:56.78                 13,
12:34:56.78                 14,
12:34:56.78                 15,
12:34:56.78                 16,
12:34:56.78                 17,
12:34:56.78                 18,
12:34:56.78                 19,
12:34:56.78                 20,
12:34:56.78                 21,
12:34:56.78                 22,
12:34:56.78                 23,
12:34:56.78                 24,
12:34:56.78                 25,
12:34:56.78                 26,
12:34:56.78                 27,
12:34:56.78                 28,
12:34:56.78                 29]
12:34:56.78   15 |     pp(dict.fromkeys(range(30), 4))
12:34:56.78 LOG:
12:34:56.78 .... dict.fromkeys(range(30), 4) = {0: 4,
12:34:56.78                                     1: 4,
12:34:56.78                                     2: 4,
12:34:56.78                                     3: 4,
12:34:56.78                                     4: 4,
12:34:56.78                                     5: 4,
12:34:56.78                                     6: 4,
12:34:56.78                                     7: 4,
12:34:56.78                                     8: 4,
12:34:56.78                                     9: 4,
12:34:56.78                                     10: 4,
12:34:56.78                                     11: 4,
12:34:56.78                                     12: 4,
12:34:56.78                                     13: 4,
12:34:56.78                                     14: 4,
12:34:56.78                                     15: 4,
12:34:56.78                                     16: 4,
12:34:56.78                                     17: 4,
12:34:56.78                                     18: 4,
12:34:56.78                                     19: 4,
12:34:56.78                                     20: 4,
12:34:56.78                                     21: 4,
12:34:56.78                                     22: 4,
12:34:56.78                                     23: 4,
12:34:56.78                                     24: 4,
12:34:56.78                                     25: 4,
12:34:56.78                                     26: 4,
12:34:56.78                                     27: 4,
12:34:56.78                                     28: 4,
12:34:56.78                                     29: 4}
12:34:56.78   16 |     pp.deep(lambda: BadRepr() and 1)
12:34:56.78 LOG:
12:34:56.78 ............ BadRepr = <class 'tests.samples.pp.BadRepr'>
12:34:56.78 ........ BadRepr() = <Exception in repr(): ValueError: bad>
12:34:56.78 .... BadRepr() and 1 = 1
12:34:56.78   17 |     pp.deep(lambda: 1 / 2)
12:34:56.78 LOG:
12:34:56.78 .... 1 / 2 = 0.5
12:34:56.78   19 |     try:
12:34:56.78   20 |         pp.deep(lambda: max(y + 2, (y + 3) / 0))
12:34:56.78 LOG:
12:34:56.78 ............ y = 2
12:34:56.78 ........ y + 2 = 4
12:34:56.78 ................ y = 2
12:34:56.78 ............ y + 3 = 5
12:34:56.78 ........ (y + 3) / 0 = !!! ZeroDivisionError!
12:34:56.78 !!! ZeroDivisionError: division by zero
12:34:56.78 !!! When calling: pp.deep(...)
12:34:56.78   21 |     except ZeroDivisionError:
12:34:56.78   22 |         pass
12:34:56.78 <<< Return value from main: None
"""
