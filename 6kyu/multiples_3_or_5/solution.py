def find_multiples(n: int) -> int:
    """Find the multiples of 3 and 5 below n and return the sum."""
    numbers = [number for number in range(1, n) if number % 3 == 0 or number % 5 == 0]
    print(numbers)
    return sum(numbers)
