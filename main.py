print("You now have three options you are able to preceed with.\nType the corresponding number you want to be performed.\nLEARNING MODE - 1\nVALIDATION MODE - 2\nWITHOUT ANY MODE - 3") #maybe help too
choice = ""

while choice != "exit":
    choice = input()
    if choice == "1":
        print("Learning mode will be executed.")
        break
    elif choice == "2":
        print("Validation mode will be executed.")
        break
    elif choice == "3":
        print("The request will be send directly to the server.")
        break
    elif choice == "exit":
        print("The process will be exited.")
        break
    else:
        print("The number you have chosen does not match with any mode option. You can try again or quit by writing exit.")