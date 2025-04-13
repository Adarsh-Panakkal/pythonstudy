try:
    age = int(input("Age:"))
    income = 200000
    risk =income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("invalid value.")