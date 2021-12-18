# Helpful in repeating and retrying

for number in range(1,10,2):
    print("Attempt",number + 1, (number + 1) * ".")
    
success = True
for i  in range(7):
    print("Attempt")
    if success:
        print("successful")
        break

else: 
    print("Attempted but failed")