#Username and password problem

def user_details(user_input,password_input):
    file_object = open("details.txt","w+")
    text = f"User name is - {user_input}\n"
    text_2 = f"The password is -{password_input}"
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
            file_open = open ("shopping-cart.txt","r")
            print(file_open)
            file_open.close()
        else:
            count += 1


list_of_items = []
for value,keys in dict_of_items.items():
    list_of_items.append([value,keys])
print(list_of_items)

#to add,remove items from the cart


