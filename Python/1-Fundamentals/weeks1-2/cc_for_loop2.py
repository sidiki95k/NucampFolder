for x in range(0, 1, 7):
    if x == "0 or 6":
        print(x)

if x == 1:
    print("One asterisk")
elif x == 5:
    print("Five asterisks")
else:
    print(not 1 or 5)

if x == 2 or x == 5:
    print("two asterisks")
elif x == 2:
    print("Not 1 or 5, but x is 2")
else:
    print("Not 1, 2, or 5")

if x == 1 or x == 5:
    print("Two asterisks")
elif x == 2 or x == 3:
    print("Three asterisks")
else:
    print("Not 1, 2, 3, or 5")


if x == 1 or x == 5:
    print("wo asterisks")
elif x == 2 or x == 3:
    print("Three asterisks")
else:
    print("Four asterisks")
