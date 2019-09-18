import re
import os.path
from os import path

def register_name_password():
    input_username = input("enter your username : ")
    input_password = input("Enter your password : ")
    if (len(input_username)>8):
        print("ok")
    else:
        print("Please enter username atleast 8 character ")

    result = True
    if (len(input_password) < 8):
        result = False
    elif not re.search("[a-z]", input_password):
        result = False
    elif not re.search("[A-Z]", input_password):
        result = False
    elif not re.search("[0-9]", input_password):
        result = False
    else:
        print("password is verified")
    # if result == False:
    #     print("Not a Valid Password")

    file_name = input_username+'.txt'

    if str(path.isfile(file_name)) == True:
        print("you are already registered")
    else:
        list_user[input_username] = input_password
        result = str(list_user)
        login_file = open('input_username.txt', 'a')
        login_file.write(result)
        print(list_user)
        login_file.close()



def login(input_username,input_password):
    input_username = input("enter your username : ")
    input_password = input("Enter your password : ")
    if str(path.isfile('input_username.txt'))==True:
        open_user_file=open('input_username.txt','r')
        open_user_file.read()

def create_shopping_cart():
        create_shoppingcard=open('input_username_shopping-cart.txt','a')
        serial_number=int(input("Enter the serial number : "))
        items_name=input("enter items name")
        shopping_list[serial_number]=items_name
        items_list=str(shopping_list)
        create_shoppingcard.write(items_list)
def view_shopping_cart():

    retrive_shopping_cart=open('input_username_shopping.txt','r')
    print(retrive_shopping_cart.read())



def add_new_items():

    new_items = input("Enter the itrms name :")
    shopping_list.append(new_items)
    return shopping_list

def remove_items():
    items_name = input("enter items name")
    del shopping_list[items_name]
    return shopping_list


def edit_items():
    new_items = input("enter items name")
    shopping_list.update(new_items)
    return shopping_list

list_user={}
shopping_list={}



while True:
    select = input("Select operations form New_user, login ,create_shopping-cart, add_items, remove_items, edit_items ,logout :")

    if select == 'New_user':
        register_name_password()

    elif select == 'login':
        login()
    elif select == 'create_shopping-cart':
        create_shopping_cart()

    elif select == 'add_items':
        add_new_items()

    elif select == 'remove_items':
        remove_items()
    elif select == 'logout':
        continue
    else:
        print("Invalid input")
        break