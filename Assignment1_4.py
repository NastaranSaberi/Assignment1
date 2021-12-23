Name = input(" Please enter your name:")
Family = input("Please enter your family:")
A = float(input("Math score:"))
B = float(input("Language score:"))
C = float(input("Chemistry score:"))

average = (A + B + C) / 3


if average >= 17 :
     print(Name , Family ,"your educational status is Great.")

if (average < 17) and (average >= 12) :
    print(Name , Family ,"your educational status is Normal.")
    

if average < 12 :
     print(Name , Family ,"your educational status is Fail.")
   



