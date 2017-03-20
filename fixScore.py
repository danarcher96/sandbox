"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def calc_result(score):
    if score < 0 or score > 100:
        print("Invalid score")

    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result



score = float(input("Enter score: "))
result = calc_result(score)
print(result)