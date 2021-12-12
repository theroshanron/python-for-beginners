#How to handle errors
try:
    age = int(input(" What is your Age: "))
    income  = 2000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value")
except KeyError:
    print("Wrong Key")
except ZeroDivisionError:
    print(" You can't put age as Zero")