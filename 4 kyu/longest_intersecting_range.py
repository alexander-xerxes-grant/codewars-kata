data = [[1, 2], [6, 10], [11, 15]]
data8 = [(1, 5), (6, 10)]
data5 = [(1, 5)]
data19 = ([1, 5], [10, 20], [1, 6], [16, 19], [5, 11])


def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a, b in sorted(intervals):
        if top < a:
            top = a
        if top < b:
            s, top = s + b - top, b
    return s


print(sum_of_intervals(data), "should be 9")
print(sum_of_intervals(data5), "should be 4")
print(sum_of_intervals(data8), "should be 8")
print(sum_of_intervals(data19), "should be 19")
