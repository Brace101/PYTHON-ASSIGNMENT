for day in range(1, 13):

    print("On the ", end="")

    # Switch for day names
    match day:
        case 1: print("first", end="")
        case 2: print("second", end="")
        case 3: print("third", end="")
        case 4: print("fourth", end="")
        case 5: print("fifth", end="")
        case 6: print("sixth", end="")
        case 7: print("seventh", end="")
        case 8: print("eighth", end="")
        case 9: print("ninth", end="")
        case 10: print("tenth", end="")
        case 11: print("eleventh", end="")
        case 12: print("twelfth", end="")

    print(" day of Christmas my true love gave to me:")

    # Gifts (cumulative)
    if day >= 12: print("Twelve drummers drumming,")
    if day >= 11: print("Eleven pipers piping,")
    if day >= 10: print("Ten lords a-leaping,")
    if day >= 9:  print("Nine ladies dancing,")
    if day >= 8:  print("Eight maids a-milking,")
    if day >= 7:  print("Seven swans a-swimming,")
    if day >= 6:  print("Six geese a-laying,")
    if day >= 5:  print("Five gold rings,")
    if day >= 4:  print("Four calling birds,")
    if day >= 3:  print("Three French hens,")
    if day >= 2:  print("Two turtle doves,")

    if day == 1:
        print("A partridge in a pear tree.")
    else:
        print("And a partridge in a pear tree.")

    print()

