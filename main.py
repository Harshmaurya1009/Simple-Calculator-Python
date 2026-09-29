num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

opr = int(input("""Select operation
1. addition
2. subtraction
3. multiplication
4. division
5. exit
:- """))

while opr != 5:
    if opr == 1:
        print(f"sum is: {num1 + num2}")

    elif opr == 2:
        print(f"difference is: {num1 - num2}")

    elif opr == 3:
        print(f"product is: {num1 * num2}")

    elif opr == 4:
        if num2 == 0:
            print("denominator cannot be zero!!")
        else:
            print(f"quotient is: {num1 / num2}")

    else:
            print("invalid value")

    opr = int(input("""Select operation
1. addition
2. subtraction
3. multiplication
4. division
5. exit
:- """))