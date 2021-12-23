Weight = float(input("Please write your weight in kilograms:"))
Height = float(input("Please write your height in meters:"))
 
BMI = Weight / Height**2


if BMI <18.5 :
    result = "Body mass index : UNDERWEIGHT"

if (BMI > 18.5) and (BMI < 24.9):
    result = "Body mass index : NORMAL"

if (BMI > 25) and (BMI < 29.9):
    result = "Body mass index : OVERWEIGHT"

if (BMI > 30) and (BMI < 34.9):
    result = "Body mass index : OBESE"

if BMI > 35 :
    result = "Body mass index : EXTREMELY OBESE"


print(result)

