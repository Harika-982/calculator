def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if a!=0:
        return a/b
    else:
        return("cannot be divided")
print("Select the operation that need to be performed")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=input("Enter your choice")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if choice == '1':
    print(a, "+", b, "=", addition(a,b))
elif choice == '2':
    print(a, "-", b, "=", subtraction(a,b))
elif choice == '3':
    print(a, "*", b, "=", multiplication(a,b))
elif choice == '4':
    print(a, "/",b, "=", division(a,b))
else:
    print("Invalid input")