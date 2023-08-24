def onlyint(msg):  
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[031mPlease, enter an integer number.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[031mThe user prefered not to enter anything.\033[m")
        else:
            return n
        
def onlyfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[031mPlease, enter a real number.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[031mThe user prefered not to enter anything.\033[m")
        else:
            return n

n = onlyint("Enter an integer number: ")
print(f"\033[032mYou entered the number {n}.\033[m")

n = onlyfloat("Enter a real number: ")
print(f"\033[032mYou entered the number {n}.\033[m")

