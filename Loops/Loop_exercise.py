# Helpful in repeating and retrying

for number in range(1,10,2):
    print("Attempt",number + 1, (number + 1) * ".")
    
    
    
#For else
success = True
for i  in range(7):
    print("Attempt")
    if success:
        print("successful")
        break

else: 
    print("Attempted but failed")
    
    
#Nested Loops

for x in range (3):
    for y in range (2):
        print("Hello",x,y)
        
#iteration
print(type(5))
print(type(range(5)))
print(range(5))

for x in "Anaconda":
    print(x)
    
for y in range(4):
    print(y)
    
for z in [3,4,5]:
    print(z)
    
#strings, list and range are iterable

shopping_cart = ['colgate','potato','soap']
for n in shopping_cart:
    print(n)