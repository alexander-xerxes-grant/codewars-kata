# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    year = [m for m in range(1, 13)]
    # print(year)
    Q1 = year[:3]
    Q2 = year[3:6]
    Q3 = year[6:9]
    Q4 = year[9:12]

    if month in Q1:
        return 1
    elif month in Q2:
        return 2
    elif month in Q3:
        return 3
    else:
        return 4

print(quarter_of(3))
print(quarter_of(8))
print(quarter_of(11))