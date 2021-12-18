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
    
    
#loop over the list
letters = ["a","b","c","d"]
items = [0,"A"]
for index,p in enumerate(letters): #enumerate gives tuple and index
    print(index,p)
    
    
#strings, list and range are iterable

shopping_cart = ['colgate','potato','soap']
for n in shopping_cart:
    print(n)
    
count_even = 0
for i in range(10):
    if i%2 == 0:
        print(i)
        count_even += 1
print(f'We have {count_even} even numbers!')