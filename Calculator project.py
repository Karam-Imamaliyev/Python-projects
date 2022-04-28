#Add function
def add(x, y):

   return x + y

#Subtract function
def subtract(x, y):

   return x - y

#Multiple function
def multiply(x, y):

   return x * y

#Divide Function
def divide(x, y):

   return x / y

num1 = int(input("First number: "))

choice = input('Operation: ')

num2 = int(input("Second number: "))

if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")