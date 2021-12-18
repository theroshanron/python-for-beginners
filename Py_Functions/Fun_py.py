#how to write own functions
#To reduce the lines of code in a single file so that it's easier to maintain and reusable

from types import MemberDescriptorType, resolve_bases


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

# **arg

def save_user(**user): # Multiple key value pair is accepted
    print(user)
    print(user["last_name"])
    
    
save_user(id=1,first_name = "Roshan", last_name = "Chaudahry") #Will give a dictionary

message = "c" #Global variable and accessible everywhere and stays in the memory for a longer period of time
#Scope
def greet(name):
    global message
    message ="a"  #knows as local variable and exists only in this function
    
    
def greet2(name):
    message ="b" 
    
"""print(message) #message is not defined """

print(greet("Roshan")) #returns none
z=greet("Mohan")
print(message) #Will get global variable


#Fizz Buzz Algorithm

def fizz_buzz(input):
    if (input % 5 == 0 and input % 3 == 0):
            return "Buzz Fizz"
        
    if input % 3 == 0:
            return "Fizz"
    if input % 5 == 0:
            return "Buzz"
       
    
    return(input)

print(fizz_buzz(7))
print(fizz_buzz(9))
print(fizz_buzz(15))
print(fizz_buzz(5))
print(fizz_buzz(4))
