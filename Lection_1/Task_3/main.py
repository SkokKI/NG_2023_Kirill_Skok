First_Number = int (input("Input first number\n"))
Second_Number = int (input("Input second number\n"))
Math_Action = input("Input math action \"+\", \"-\", \"*\" or \"/\"\n")
match Math_Action:
    case "+":
        print(First_Number,"+",Second_Number,"=", First_Number+Second_Number)
    case "-":
        print(First_Number,"-",Second_Number,"=", First_Number-Second_Number)
    case "*":
        print(First_Number,"*",Second_Number,"=", First_Number*Second_Number)
    case "/":
        print(First_Number,"/",Second_Number,"=", First_Number/Second_Number)
    case _:
        print("There is no such math action")