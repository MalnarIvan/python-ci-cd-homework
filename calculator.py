def factorial(n: int) -> int:
    """
    Calculates factorial of a non-negative integer.
    """
    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
