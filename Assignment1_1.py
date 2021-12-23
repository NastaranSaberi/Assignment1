import math
op = input("Operation:")


if op == "+":
    A = float(input("Please enter first number:"))
    B = float(input("Please enter second number:"))
    result = A + B

if op == "-":
    A = float(input("Please enter first number:"))
    B = float(input("Please enter second number:"))
    result = A - B

if op == "*":
    A = float(input("Please enter first number:"))
    B = float(input("Please enter second number:"))
    result = A * B

if op == "/":
    A = float(input("Please enter first number:"))
    B = float(input("Please enter second number:"))
    if B == 0:
        result = "Error!!!!!"
    else:
        result = A / B

if op == "radical":
    A = float(input("Please enter number:"))
    result = math.sqrt(A)


if op == "cos":
    A = input("degree or radian?")
    if A == "degree":
        B = float(input())
        result = math.cos(math.radians(B))
   
    if A == "radian":
        B = float(input())
        result = math.cos(B)


if op == "sin":
    A = input("degree or radian?")
    if A == "degree":
        B = float(input())
        result = math.sin(math.radians(B))
    
    if A == "radian":
        B = float(input())
        result = math.sin(B)


if op == "tan":
    A = input("degree or radian?")
    if A == "degree":
        B = float(input())
        result = math.tan(math.radians(B))
    
    if A == "radian":
        B = float(input())
        result = math.tan(B)


if op == "cot":
    A = input("degree or radian?")
    if A == "degree":
        B = float(input())
        result = 1/math.tan(math.radians(B))
    
    if A == "radian":
        B = float(input())
        result =1/ math.tan(B)


if op == "factorial":
    A = int(input("Please enter number:"))
    result = math.factorial(A)




 
print(result)