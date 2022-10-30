import math

starter = input("Hi, for if method please enter 1 for switch please enter 2 :\n")

if starter == "1":

    x = input("""
        "please enter your operation number: \n 
        1:*: for adding \n 
        2:*: for subtracting \n 
        3:*: for multiplying \n 
        4:*: for division \n 
        5:*: for power \n 
        6:*: is square root \n
        """)

    if x == "1":
        towInput = j, i = input(
            "enter your tow number with white space between ").split()
        print(int(j) + int(i))

    elif x == "2":
        towInput = j, i = input(
            "enter your tow number with white space between ").split()
        print(int(j) - int(i))

    elif x == "3":
        towInput = j, i = input(
            "enter your tow number with white space between ").split()
        print(int(j) * int(i))

    elif x == "4":
        towInput = j, i = input(
            "enter your tow number with white space between ").split()
        if int(i) == 0:
            print("you cant divide by 0")
        else:
            print(int(j) / int(i))

    elif x == "5":
        powerInput = x, y = input("enter your base then your power: ").split()
        print(math.pow(int(x), int(y)))

    elif x == "6":
        oneInput = input("enter your number: ")
        print(math.sqrt(int(oneInput)))
if starter == "2":

    option = input("""
        "please enter your operation number: \n 
        1:*: for adding \n 
        2:*: for subtracting \n 
        3:*: for multiplying \n 
        4:*: for division \n 
        5:*: for power \n 
        6:*: is square root \n
        """)

    match option:
        case "1":
            towInput = j, i = input(
            "enter your tow number with white space between ").split()
            print("result =" ,int(j) + int(i))

        case "2":
            
             towInput = j, i = input(
            "enter your tow number with white space between ").split()
             print("result =" ,int(j) - int(i))
        
        case "3":
            option == "3"
            towInput = j, i = input(
            "enter your tow number with white space between ").split()
            print("result =" ,int(j) * int(i))

        case "4":
            
            towInput = j, i = input(
            "enter your tow number with white space between ").split()
            if int(i) == 0:
                print("you cant divide by 0")
            else:
                 print("result =" ,int(j) / int(i))

        case "5":
            
            powerInput = x, y = input("enter your base then your power: ").split()
            print("result =" ,math.pow(int(x), int(y)))

        case "6":
            
            oneInput = input("enter your number: ")
            print("result =" ,math.sqrt(int(oneInput)))




