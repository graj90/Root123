def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))



if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")
    def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

print("Select conversion:")
print("1. KG to Pounds")
print("2. Pounds to KG")

choice = input("Enter choice (1/2): ")

if choice == '1':
    kg = float(input("Enter weight in KG: "))
    pounds = kg_to_pounds(kg)
    print(kg, "KG =", pounds, "Pounds")
elif choice == '2':
    pounds = float(input("Enter weight in Pounds: "))
    kg = pounds_to_kg(pounds)
    print(pounds, "Pounds =", kg, "KG")
else:
    print("Invalid Input")

print "That is everythong we need"
print "we need to add some functtion and need to push in hub"