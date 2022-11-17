




# # def sum_intervals(data):
# #     intervals = []
# #     for pair in data:
# #         for index in range(pair[0], (pair[1]+ 1)):
# #             intervals.append(index)
# #     set_of_intervals = list(set(sorted(intervals))
# #     length = 0
# #     for item in set_of_intervals:
# #         if item == (set_of_intervals[item - 1] + 1):
# #             print(item)
# #             length + 1
# #         else:
# #             length = 0
# #     return length

# # print(sum_intervals(data))
# # print(sum_intervals(data8), "should be 8")
# # print(sum_intervals(data5), "should be 5")




# def sum_of_intervals(array_of_intervals):

    # # Define sum of intervals and count

    # intervals = []
    # for pair in array_of_intervals:
    #     for index in range(pair[0], (pair[1]+ 1)):
    #         intervals.append(index)

    # # Sort the array

    # sorted_array_of_intervals = sorted(intervals)
    # # print(sorted_array_of_intervals)

    # # Remove duplicate elements
    # deduped_array = []
    
    # for index in range(0, len(sorted_array_of_intervals)):
    #     if sorted_array_of_intervals[index] != sorted_array_of_intervals[index - 1]:
    #         deduped_array.append(sorted_array_of_intervals[index])
    
    # print(deduped_array)
    # # Find the longest subsequence

    # count = 0

    # for i in range(1, len(deduped_array)):
    #     print(i, "current index")
    #     if (i > 0 and deduped_array[i] == deduped_array[i - 1] + 1):
    #         count += 1
    #         print(count, "current count")
    #     else:
    #         count = 1
    #         print(count, "resetting count")
    # return count
            


data = [[1, 2], [6, 10], [11, 15]]
data8 = [(1, 5), (6, 10)]
data5 = [(1, 5)]



def sum_of_intervals(array_of_intervals):

    # # Create new array of intervals combined

    # intervals = []

    # for pair in array_of_intervals:
    #     for index in range(pair[0], (pair[1])):
    #         intervals.append(index)
    # return len(set(intervals))
    return len(set({i for a,b in array_of_intervals for i in range(a,b)}))


print(sum_of_intervals(data), "should be 9")
print(sum_of_intervals(data5), "should be 4")
print(sum_of_intervals(data8), "should be 8")