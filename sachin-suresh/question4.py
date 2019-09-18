import os
from os import path
from ast import literal_eval

def register():
    print("Welcome to user registration")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    os.mkdir(username)
    registry_file = open(username + '/password.txt', 'a')
    registry_file.write(password)
    registry_file.close()

def login():
    log = False
    print("Enter your credentials below")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if path.exists('/home/sachin/tarzan/evaluations/sachin-suresh/'+username+"/password.txt"):
        log = True
        registry_file = open('/home/sachin/tarzan/evaluations/sachin-suresh/'+username+'/password.txt', 'r')
        registry = registry_file.read()
        if log and password == registry:
            log = True
        else:
            log = False
    return log, username

def display_cart(username):
    shopping_cart = open('/home/sachin/tarzan/evaluations/sachin-suresh/' + username + '/shopping_cart.txt', 'r')
    item_list = shopping_cart.read().split()
    print("Your shopping cart has")
    for i in item_list:
        item_dict = literal_eval("{'a': 1}")
        item_name = item_dict.items(0)
        item_num = item_dict.items(1)
        print(item_name,item_num)
    shopping_cart.close()

def add_to_cart(username):
    dictionary = {}
    case = 'y'
    shopping_cart = open('/home/sachin/tarzan/evaluations/sachin-suresh/' + username + '/shopping_cart.txt', 'a+')
    while (case == 'y'):
        item_name = input("Enter the item you want to add to the cart: ")
        item_num = int(input("Enter the quantity of item you want: "))
        dictionary[item_name] = item_num
        shopping_cart.write(str(dictionary))
        check = input("Do you want to continue? Enter y to continue")
        if check == 'y':
            continue
        else:
            break
    shopping_cart.close()
    display_cart(username)

def remove_from_cart(username):
    item_name = input("Enter the item you want to remove from the cart: ")
    shopping_cart = open('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart.txt', 'a+')
    shopping_cart_new = open('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart_new.txt', 'a+')
    shopping_cart.seek(0,0)
    while (1):
        item = shopping_cart.read()
        if item == '':
            break
        item_list = item.split()
        if item_list[0] != item_name:
            shopping_cart_new.write(item)
    shopping_cart.close()
    shopping_cart_new.close()
    os.remove('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart.txt')
    os.rename('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart_new.txt','/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart.txt')

def edit_quantity(username):
    item_name = input("Enter the item you want to edit in quantity: ")
    item_num = int(input("Enter the new quantity of item: "))
    shopping_cart = open('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart.txt', 'a+')
    shopping_cart_new = open('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart_new.txt', 'a+')
    shopping_cart.seek(0, 0)
    while (1):
        item = shopping_cart.read()
        if item == '':
            break
        item_list = item.split()
        if item_list[0] != item_name:
            shopping_cart_new.write(item)
        else:
            shopping_cart_new.write(str([username,item_name,item_num]))
    shopping_cart.close()
    shopping_cart_new.close()
    os.remove('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart.txt')
    os.rename('/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart_new.txt','/home/sachin/tarzan/evaluations/sachin-suresh/shopping_cart.txt')

def logout():
    print("You are logged out")

def delete_account(username):
    check = input("Are you sure you want to delete all the data from your account? Press y to continue: ")
    if check == 'y':
        registry_file = open('/home/sachin/tarzan/evaluations/sachin-suresh/reg_file.txt', 'r')
        registry_file_new = open('/home/sachin/tarzan/evaluations/sachin-suresh/reg_file_new.txt', 'r')
        while (1):
            registry = registry_file.read()
            if registry == '':
                break
            registry_list = registry.split()
            if username not in registry_list:
                registry_file_new.write(str([username,))
        registry_file.close()
        registry_file_new.close()
        os.remove('/home/sachin/tarzan/evaluations/sachin-suresh/reg_file.txt')
        os.rename('/home/sachin/tarzan/evaluations/sachin-suresh/reg_file_new.txt.txt',
                  '/home/sachin/tarzan/evaluations/sachin-suresh/reg_file.txt')
    else:
        print("Delete operation aborted!")

logged = True #False
username = 'default'
print("Shopping App")
user_input = input("Enter your choice:\n1.Register\n2. Login\n3. Add to cart\n4. Remove from Cart\n5. Edit quantity of items\n6. Logout\n7.Delete Account")
if user_input == '1':
    register()
elif user_input == '2':
    logged, username = login()
    if(logged==True):
        print("You are logged in")
    else:
        print("Invalid credentials.")
elif user_input == '3':
    if logged == True:
        add_to_cart('sachin') #username
    else:
        print("User not logged in. Please login")
elif user_input == '4':
    if logged == True:
        remove_from_cart(username)
    else:
        print("User not logged in. Please login")
elif user_input == '5':
    if logged == True:
        remove_from_cart(username)
    else:
        print("User not logged in. Please login")
elif user_input == '6':
    if logged == True:
        edit_quantity(username)
    else:
        print("User not logged in. Please login")
elif user_input == '7':
    if logged == True:
        logout()
    else:
        print("User already logged out")
elif user_input == '8':
    if logged == True:
        delete_account(username)
    else:
        print("User not logged in. Please login")
else:
    print("Invalid input")

