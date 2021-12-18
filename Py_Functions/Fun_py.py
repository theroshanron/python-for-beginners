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
