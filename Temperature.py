"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Daniel Arhcer'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def calc_farenheit():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Results: {:.2f} C".format(celsius))


def calc_celsius():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


while choice != "Q":
    if choice == "C":
        calc_celsius()
    elif choice == "F":
        calc_farenheit()

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")