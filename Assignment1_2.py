A = float(input("First Side:"))
B = float(input("Second Side:"))
C = float(input("Third Side:"))


if (C < A + B) and (A < B + C) and (B < A + B):
    result = "You can make a triangle with these sides."
else:
    result = "You can not make a triangle with these sides"


print(result)