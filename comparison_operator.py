temperature = 30

if temperature > 30:
    print("Hot hot hot")
else:
    print("Bleh!")


if temperature < 30:
    print("Hot hot hot")
else:
    print("Bleh!")


if temperature <= 30:
    print("Hot hot hot")
else:
    print("Bleh!")

if temperature == 30:
    print("Hot hot hot")
else:
    print("Bleh!")

#Exercise

name = input("What is your name ")
name_of_ancient = input("What was your name initially ? ")

if len(name)<3 :
    print("Name should be of at least 3 characters")
elif len(name_of_ancient)>10:
    print("Name can be of max 10 characters")
else:
    print("Very well my boy!")

