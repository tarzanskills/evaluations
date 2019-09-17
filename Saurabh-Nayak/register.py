#Username and password problem

dict_of_user = {}

def user_details(user_input,password_input):
    file_object = open("details.txt","w+")
    text = f"User name is - {user_input}\n"
    text_2 = f"The password is -{password_input}"
    dict_of_user[text] = text_2
    file_object.write(text)
    file_object.write(text_2)
    file_object.close()


user_input = input("Enter your name : ")
password_input = input("Enter your password : ")

user_details(user_input,password_input)

#to login using same password and username

def login():
    print("There are only 10 trials to login :")
    count = 10
    while 0<10:
        user_name = input("Enter your name : ")
        user_password = input("Enter your password : ")
        if user_name == user_input and user_password == password_input:
            print("Welcome to the shopping world")
            break
        else:
            count += 1
login()

number = int(input("Enter the number of items : "))
file_objective = open("shopping-cart.txt", "w+")
dict_of_items = {}
for i in range(0, number):
    items= input("Enter the list of items : ")
    quantity= int(input("Enter the quantity : "))
    dict_of_items[items] = quantity
print(dict_of_items)
file_objective.write(str(dict_of_items))
file_objective.close()

#to retrieve the login

def retrieve_login():
    print("There are only 5 trials to login :")
    count = 5
    while 0<5:
        user_name = input("Enter your name : ")
        user_password = input("Enter your password : ")
        if user_name == user_input and user_password == password_input:
            print("Welcome to the shopping world")
            file_open = open ("shopping-cart.txt","a+")
            print(file_open)
            file_open.close()
        else:
            count += 1


list_of_items = []
for value,keys in dict_of_items.items():
    list_of_items.append([value,keys])
print(list_of_items)

#to add,remove items from the cart
def change_in_items():
    item_number_add = int(input("Enter the number of items to be added :"))
    item_number_remove = int(input("Enter the number of items to be removed : "))
    add_remove = input("Do you like to add or remove the items : ")
    if add_remove == 'add':
        for i in range(0,item_number_add):
            item_add = input("Enter the item to be added : ")
            item_quantity = int(input("Enter the quantity : "))
            list_of_items.append([item_add,item_quantity])

    elif add_remove == 'remove':
        for j in range(0,item_number_remove):
            item_remove = input("Enter the item to remove :")
            item_remove_quantity = int(input("Enter the quantity"))
            list_of_items.remove([item_remove,item_remove_quantity])

print("Do the necessary changes required with the list of items ")
change_in_items()

#to change the Quantity

def change_in_quantity():
    print(list_of_items)
    print("Do the changes required in the list of items ")
    number_of_quantity = int(input("Enter the number of quantity to be changed: "))
    for i in range(0,number_of_quantity):
        items_of_quantity = input("Enter the item of which quantity to be changed: ")
        quantity_to_be_changed= int(input("Enter the quantity :"))
        dict_of_items[input(items_of_quantity)]= quantity_to_be_changed

change_in_quantity()

def logout():
    log_user = input("Please type 'logout' to exit : ")
    if log_user == 'logout':
        exit()

