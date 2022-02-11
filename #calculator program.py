# calculator program
num1 = int(input("Pls enter the first number: "))
num2 = int(input("Pls enter the second number: "))

add = "Sum of two numbers is: "
subtract = "Difference between two numbers is: "
multiply = "Product of two numbers is: "
divide = "Quotient of two numbers is: "

print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("select your operation choice: "))

if(choice == 1):
    print(add, num1 + num2)

elif(choice == 2):
    print(subtract, num1 - num2)

elif(choice == 3):
    print(multiply, num1 * num2)

elif(choice == 4):
    print(divide, num1 / num2)
