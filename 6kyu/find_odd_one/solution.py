def find_odd_one(array):
    odds = [number for number in array if number % 2 != 0]
    evens = [number for number in array if number % 2 == 0]

    return odds[0] if len(odds) < len(evens) else evens[0]
