started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car has already started!!!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car has already stopped")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        print("""
start - to start
stop - to stop the car
quit - to exit the car""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")





