# Exercise for car game
print("type help to understand ")
user_value = input("Ready to start the game? ")
value = user_value.lower()
command =""

started = False


while True:
    command = input("> ").lower()
    if command== "start":
        if started:
            print("Car is already started! ")
        else:
            started = True
            print("Car started.. Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started=False
            print("Car stopped.. !")
    elif command  == "help":
        print(""" 
start - to start the game
stop - to stop the car
quit - to exit the game """)
    elif command == "quit":
        break
    else:
        print("I don't understand that")

