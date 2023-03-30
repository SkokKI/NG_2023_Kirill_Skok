import math
Number_a = float (input("Input a\n"))
Number_b = float (input("Input b\n"))
Number_c = float (input("Input c\n"))
if Number_a == 0:
    Single_root = (-Number_c)/Number_b
    print("Your root =",Single_root)
else:
    Discriminant = Number_b**2 - 4*Number_a*Number_c
    print("Yout discriminant =",Discriminant)
    if Discriminant < 0:
        print("This equation has no roots")
    elif Discriminant == 0:
        Single_root = -Number_b/(2*Number_a)
        print("Your root =",Single_root)
    else:
        First_root = (-Number_b-math.sqrt(Discriminant))/(2*Number_a)
        Second_root = (-Number_b+math.sqrt(Discriminant))/(2*Number_a)
        print("Your first root =",First_root)
        print("Your second root =",Second_root)

