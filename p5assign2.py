
N1 = float(input("Enter the first number: "))
N2 = float(input("Enter the second number: "))
N3 = float(input("Enter the third number: "))



if (N1 <= N2) and (N1 <= N3):
    print(f"{N1} is the smallest number.")

elif (N2 <= N1) and  (N2 <= N3):
    print(f"{N2} is the smallest number.")

else:
    print(f"{N3} is the smallest number.")
