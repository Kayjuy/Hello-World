def circleArea(radius):
    pi = 3.14159
    return pi * radius ** 2


def calculateTax(money, tax):
    return money + (money * tax)


def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# Circle
radius = float(input("Enter radius: "))
print(f"{circleArea(radius):.2f}")

# Taxes
money = float(input("Enter money: "))
tax = float(input("Enter tax rate: "))
print(f"{calculateTax(money, tax / 100):.2f}")

# Temperature
fahrenheit = float(input("Enter Fahrenheit: "))
print(fahrenheitToCelsius(fahrenheit))