# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

import phonenumbers

def create_phone_number(list_of_ints):
    temp_list = [int for int in list_of_ints]
    return f"({temp_list[0]}{temp_list[1]}{temp_list[2]}) {temp_list[3]}{temp_list[4]}{temp_list[5]}-{temp_list[6]}{temp_list[7]}{temp_list[8]}{temp_list[9]}"




print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
# print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))