

# 1. Userdetails area
print("Welcome to the sample shopping cart")

print("Click 1 for registering as a new user")
choice = int(input("Enter Choice:- "))

def user_registration():
    first_name = str(input("Enter your first name here"))
    last_name = str(input("Enter your last name here"))
    gender = str(input("Enter Male/Female"))
    date_of_birth = str(input("Enter Your DOB in Format (DD/MM/YYYY)"))
    Mob_no = str(input("Enter your 10 digit mobile number"))
    alt_mob_no = str(input("Enter alternate mobile number"))
    City = str(input("Enter your city"))
    Pin_code = str(input("Enter your city pincode here"))
    Delivery_address = str(input("Enter your complete address here"))
    user_name = input("Register your valid username here for future login")
    user_password = input("Register your password here")
    print("Re-check your given info")
    print(first_name)
    print(last_name)
    print(gender)
    print(date_of_birth)
    print(Mob_no)
    print(alt_mob_no)
    print(City)
    print(Pin_code)
    print(Delivery_address)
    print("User name and password is hidden for a security reason")

    file = open("user_info.txt", "a+")
    file.write("\n,First Name:- " + first_name)
    file.write("\n,Last Name:- "+ last_name)
    file.write("\n,Gender:- " + gender)
    file.write("\n,DOB:- " + date_of_birth)
    file.write("\n,Mobile No:- " + Mob_no)
    file.write("\n,Alt Mobile Number:- " + alt_mob_no)
    file.write("\n,City:- " + City)
    file.write("\n,Pincode:- " + Pin_code)
    file.write("\n,Delivery Address:- " + Delivery_address)
    file.write("\n,Username:- " + user_name)
    file.write("\n,Password:- " + user_password)
    file.write("\n")
    file.close()


if choice == 1:
    print("Welcome for registration")
    user_registration()

else:
    print("Sorry you can't able to registered now")
    print("For registration select the choice 1")
    print("Thankyou, Hope it will help you.")
    print()


# 2. User login area
print("Now time to Login in Sample Shopping Cart")
print()
print("Enter your Credential")
Enter_Username = input("Enter your username for login")
Enter_Password = input("Enter your Password ")

if Enter_Username == "pankajrathore9599":
    print("Username is correct")
    print("Enter Password Now")

    if Enter_Password == "mp37mc9599":
        print("password is correct")
        print("Welcome to the cart")

else:
    print("Wrong Credentials Try Again")

# 3. Shopping cart items

print("Select the items below to add in the cart")
print("Press 1 for add 'Notebook' in your cart")
print("Press 2 for add 'Pencil' in your cart")
print("Press 3 for add 'Eraser' in your cart")
print("Press 4 for add 'Sharpner' in your cart")
print("Press 5 for add 'Scale' in your cart")
print("Press 6 for add 'Exam Pad' in your cart")
print("Press 7 for add 'Book Cover' in your cart")
print("Press 8 for add 'Bag' in your cart")
print("Press 9 for add 'Stickers' in your cart")
print("Press 10 for add 'Staplers' in your cart")

item_list = []

def shopping_cart():
    item_value = int(input("Enter your choice to add iteems in cart"))
    if item_value == 1:
        item_list.append("Notebook")
    elif item_value == 2:
        item_list.append("Pencil")
    elif item_value == 3:
        item_list.append("Eraser")
    elif item_value == 4:
        item_list.append("Sharpner")
    elif item_value == 5:
        item_list.append("Scale")
    elif item_value == 6:
        item_list.append("Exam Pad")
    elif item_value == 7:
        item_list.append("Book Cover")
    elif item_value == 8:
        item_list.append("Bag")
    elif item_value == 9:
        item_list.append("Stickers")
    elif item_value == 10:
        item_list.append("Staplers")
    else:
        print("Incorrect value entered, no value will be assigned on this. please check and try again ")

shopping_cart()


print(item_list)
str_list = str(item_list)

file1 = open("shopping cart.txt", "w")
file1.write(item_list)
file1.close()






