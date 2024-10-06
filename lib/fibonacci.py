"""
Example of a simple function to compute fibonacci numbers
"""


def compute_fibonacci(n: int) -> list[int]:
    """
    Compute fibonacci numbers up to n
    """
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib: list[int] = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
