#how to write own functions
#To reduce the lines of code in a single file so that it's easier to maintain and reusable

def greet(first_name,last_name):
    print(f"Aww! Hello {first_name} {last_name}")
    print("Welcome")


greet("Roshan","Chaudhary")  
greet("Shivani","Rana")    #Requires argument eual as parameters   

#perform a task functions
#return the value
print(round(2.7))

def get_greeting(name):
    return f"Hi {name}"

x =get_greeting("Roh")
print(x)
print(get_greeting("Roh"))


#Keyword arguments

def increment(number, by):
    return number + by

r = increment(7,by=2) 
print(r)

#Default Arguments

def increment(number, by=3):
    return number + by

l = increment(7,5) 
print(l)

#optional parameter comes after required parameter

# *args, wait what?

def multiply(*numbers): #accept all arguments and gives a tuples
    print(numbers)
    total = 1
    for i in numbers:
        print(i)
        total *= i
    return total


print(multiply(2,3,4,5))

