print("Welcome to our website")

print("This website uses cookies to provide services, offer advertisements,make statistics in line with the Privacy Policy. \nUsing this page, you agree for the use of cookies according to the current browser settings.")

age=int(input("Please enter your age: "))




print("Please Sign Up!")

#SIGN UP PAGE
login=str(input("Please enter your login: "))

password=str(input("Please enter your password: "))

print("Your login is ",login,"and your password is","********",)

#SIGN IN PAGE
print("Please Sign in!")
registrated_login=str(input("Please enter your login: "))

registrated_password=str(input("Please enter your password: "))

if login==registrated_login and password==registrated_password:
    print("You successfully enter")
elif login!=registrated_login and password==registrated_password:
    print("You entered false login")
elif login==registrated_login and password!=registrated_password:
    print("You entered false password")
else:
    print("Your login and password are not correct")



