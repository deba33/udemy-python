def ask_for_int():
    while True:
        try:
            result = int(input("please provide a number: "))
        except:
            print("Sorry! that is not a number")
            continue
        else:
            print(f"Thank you for {result}")
            break
        finally:
            print("end of try/except/finally")

ask_for_int()