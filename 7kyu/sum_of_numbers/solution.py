

def get_sum(a: int, b:int ) -> int:
    """Return the sum of all numbers between a and b, inclusive."""
    return sum(i for i in range(min(a,b), max(a,b)+1))
