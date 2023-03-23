import math
Number_a = float (input("Input a\n"))
Number_b = float (input("Input b\n"))
Number_c = float (input("Input c\n"))
if Number_a < 0 or Number_b < 0 or Number_c < 0: 
    print("Under the sign of the square root can be only a positive number or zero")
else:
    print("Square root of",Number_a,"=",math.sqrt(Number_a))
    print("Square root of",Number_b,"=",math.sqrt(Number_b))
    print("Square root of",Number_c,"=",math.sqrt(Number_c))
