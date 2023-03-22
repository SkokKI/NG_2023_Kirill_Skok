import math
Number_a = float (input("Input a\n"))
Number_b = float (input("Input b\n"))
Number_c = float (input("Input c\n"))
if Number_a < 0:
    print("Under the sign of the square root can be only a positive number or zero")
else:
    Sqrt_a = math.sqrt(Number_a)
    print("Square root of",Number_a,"=",Sqrt_a)
if Number_b < 0:
    print("Under the sign of the square root can be only a positive number or zero")
else:
    Sqrt_b = math.sqrt(Number_b)
    print("Square root of",Number_b,"=",Sqrt_b)
if Number_c < 0:
    print("Under the sign of the square root can be only a positive number or zero")
else:
    Sqrt_c = math.sqrt(Number_c)
    print("Square root of",Number_c,"=",Sqrt_c)


