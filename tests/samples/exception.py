import snoop


def foo():
    raise TypeError('bad')


def bar():
    try:
        str(foo())
    except Exception:
        str(1)
        raise


@snoop(depth=3)
def main():
    try:
        bar()
    except:
        pass


if __name__ == '__main__':
    main()


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 17
12:34:56.78   17 | def main():
12:34:56.78   18 |     try:
12:34:56.78   19 |         bar()
    12:34:56.78 >>> Call to bar in File "/path/to_file.py", line 8
    12:34:56.78    8 | def bar():
    12:34:56.78    9 |     try:
    12:34:56.78   10 |         str(foo())
        12:34:56.78 >>> Call to foo in File "/path/to_file.py", line 4
        12:34:56.78    4 | def foo():
        12:34:56.78    5 |     raise TypeError('bad')
        12:34:56.78 !!! TypeError: bad
        12:34:56.78 !!! Call ended by exception
    12:34:56.78   10 |         str(foo())
    12:34:56.78 !!! TypeError: bad
    12:34:56.78 !!! When evaluating: foo()
    12:34:56.78   11 |     except Exception:
    12:34:56.78   12 |         str(1)
    12:34:56.78   13 |         raise
    12:34:56.78 !!! Call ended by exception
12:34:56.78   19 |         bar()
12:34:56.78 !!! TypeError: bad
12:34:56.78   20 |     except:
12:34:56.78   21 |         pass
12:34:56.78 <<< Return value from main: None
"""
