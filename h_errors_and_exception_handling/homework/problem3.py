def ask():
    while True:
        try:
            num = int(input("\nEnter a number: "))
        except:
            print("That is not a number.\nPlease, provide a number")
            continue
        else:
            break

    squr = num ** 2
    print(f"square of {num} is {squr}.")


ask()
