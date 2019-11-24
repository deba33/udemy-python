def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("That is not a number")
            continue
        else:
            print("Yes Thank You")
            break
        finally:
            print("Nothing to show here")


ask_for_int()
