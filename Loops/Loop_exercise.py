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