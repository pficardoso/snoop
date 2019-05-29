import snoop


@snoop.snoop()
def main():
    foo = list(range(1000))
    return foo


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 5
12:34:56.78    5 | def main():
12:34:56.78    6 |     foo = list(range(1000))
12:34:56.78 .......... foo = [0, 1, 2, ..., 997, 998, 999]
12:34:56.78 .......... len(foo) = 1000
12:34:56.78    7 |     return foo
12:34:56.78 <<< Return value from main: [0, 1, 2, ..., 997, 998, 999]
"""
