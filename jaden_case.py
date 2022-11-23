def to_jaden_case(string):

    return " ".join([word[0].upper() + word[1:] for word in string.split(" ")])


print(to_jaden_case("aa ba c'a"))


def sum_of_intervals(array_of_intervals):

    # Define sum of intervals and count

    sum = 0
    count = 0

    # Sort the array

    sort = array_of_intervals.sort()

    # Create a new array of all the numbers in the ranges of the invervals

    sorted_array_of_intervals = []

    sorted_array_of_intervals.append(sort)

    print(sorted_array_of_intervals)
    # Remove duplicate elements

    # for index in range(1, len(sorted_array_of_intervals)):
    #     if sorted_array_of_intervals[index] != sorted_array_of_intervals[index - 1]


print(sum_of_intervals(data))
# print(sum_intervals(data8), "should be 8")
# print(sum_intervals(data5), "should be 5")
