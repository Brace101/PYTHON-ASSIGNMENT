import math
pizza = print("""
____________________________________________________
PIzza TYpe  | Number of slices |Prices per Box      |    
            |                  |                    |
____________|__________________|____________________|           
1.SAPA SIZE |       4          |    2,000           |
            |                  |                    |
____________|__________________|____________________|
2.SMALL MONEY|      6          |    2,400           |
            |                  |                    |
____________|__________________|____________________|
3.BIG BOYS  |       8          |    3,000           |
            |                  |                    |
____________|__________________|____________________|              
4.ODOGWU    |       12         |    4,200           |
____________|__________________|____________________|
            
""")
pizza = input("Dear Customer, Kindly place your order: ").upper()
Number_of_people = int(input("Kindly input number of people: "))

match pizza:
    case "SAPA SIZE":
        price = 2000
        Number_of_slices = 4

    case "SMALL MONEY":
        price = 2400
        Number_of_slices = 6

    case "BIG BOYS":
        price = 3000
        Number_of_slices = 8

    case "ODOGWU":
        price = 4200
        Number_of_slices = 12

    case _:
        print("Dear Customer, you've inputted a wrong selection")
        exit()

Number_of_boxes = math.ceil(Number_of_people / Number_of_slices)
print(f"Number of boxes for everyone is: {Number_of_boxes}")

Remaning_slices = (Number_of_boxes * Number_of_slices) - Number_of_people
print(f"Remaining slices is: {Remaning_slices}")

total_price_of_each_boxes = Number_of_boxes * price
print(f"The total price for each boxes is: {total_price_of_each_boxes}")






















