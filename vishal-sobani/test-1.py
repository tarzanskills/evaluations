import os

<<<<<<< HEAD
=======
def register_your_account():
    
    username = input("Enter your username to register your account ")
    password = input("Enter your first one time password ")
    
    print("Creating your account!!!")    
    
    file = open("logindetails.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    
    if login():
    
        print("You have successfully created the account")
    
    else:
    
        print("You aren't logged in!")

def login():
    
    username = input("Please re-enter your username ")
    password = input("Please enter your password ")  
    
    for line in open("logindetails.txt","r").readlines():
    
        login_info = line.split() 
    
        if username == login_info[0] and password == login_info[1]:
    
            print("You have now logged in")

            return True

    print("Incorrect username or password please try again")
    return False        

print(register_your_account())
print(login())


num_of_items = int(input("Enter the no of items "))
>>>>>>> 2e19127c7d0bbdb414944d65d49f6f89fdb4e74e


<<<<<<< HEAD
=======

def shopping_cart(num_of_items):
       
>>>>>>> 2e19127c7d0bbdb414944d65d49f6f89fdb4e74e

# userlogged_in == True:
#
# def accesscart():
#     if user

<<<<<<< HEAD
=======
        name = str(input("Enter the name of items "))
        
        values = int(input(f"Enter the value of {name} items "))
>>>>>>> 2e19127c7d0bbdb414944d65d49f6f89fdb4e74e

def register_your_account():
    username = input("Enter your username to register your account ")
    password = input("Enter your first one time password ")

    print("Creating your account!!!")

<<<<<<< HEAD
    file = open("logindetails.txt", "a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()

    if login():

        print("You have successfully created the account")
=======
    
        total_items=sum(list_of_cart.values())
        
        print(type(list_of_cart))
        
        print("initial dictionary = ", list_of_cart)
>>>>>>> 2e19127c7d0bbdb414944d65d49f6f89fdb4e74e

    else:

        print("You aren't logged in!")


def login():
    username = input("Please re-enter your username ")
    password = input("Please enter your password ")

<<<<<<< HEAD
    for line in open("logindetails.txt", "r").readlines():

        login_info = line.split()

        if username == login_info[0] and password == login_info[1]:
            print("You have now logged in")

            return True

    print("Incorrect username or password please try again")
    return False


print(register_your_account())
print(login())

num_of_items = int(input("Enter the no of items "))






def shopping_cart(num_of_items):

    list_of_cart = {}

    for i in range(num_of_items):

        name = str(input("Enter the name of items "))

        values = int(input(f"Enter the value of {name} items "))

        list_of_cart[name] = values

        for name, values in list_of_cart.items():
            print(f"{name} {values}")

        total_items = sum(list_of_cart.values())

        # print(type(list_of_cart))

        print("your cart is  = ", list_of_cart)

    print("Your cart is  :", list_of_cart)

    print("total value of the items in cart are  ", total_items)


print(shopping_cart(num_of_items))


=======

print(shopping_cart(num_of_items))
>>>>>>> 2e19127c7d0bbdb414944d65d49f6f89fdb4e74e
