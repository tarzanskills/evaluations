import os


def user_delete_request(user_name, user_password):
    if os.path.exists(f'{user_name}.txt'):
        os.remove(f'{user_name}.txt')
        os.remove(f'{user_name}_cart.txt')
        return True
    else:
        return False


def user_cart(user_name, user_password):
    try:
        user_cart_item = {}
        user_activity_status = True
        user_cart_data = open(f'{user_name}_cart.txt', 'a+')
        while user_activity_status:
            print("Please select only respective numbers.")
            print("1.Add to cart 2.Delete from cart 3.Modify quantity 4.View Cart 5.Logout 6.Delete my Account \n")
            user_activity = int(input())
            if user_activity == 1:
                item_name = input("Enter item name: \t")
                item_quantity = input(f"Enter {item_name} quantity:\t ")
                user_cart_item[item_name] = item_quantity
                for key, value in user_cart_item.items():
                    user_cart_data.write(key+' : '+value+'\n')
                print("Your cart has:")
                user_cart_data.seek(0)
                print(user_cart_data.read())

            elif user_activity == 2:
                item_name = input("Enter item name to delete:\t")

                if item_name in user_cart_item.keys():
                    del user_cart_item[item_name]
                    print(f'{item_name} deleted!')
                    for key, value in user_cart_item.items():
                        user_cart_data.write(key + ' : ' + value + '\n')
                else:
                    print("Item not found!")

                print("Your cart has:")
                user_cart_data.seek(0)
                print(user_cart_data.read())

            elif user_activity == 3:
                item_name = input("Enter item name to modify.\t")
                item_quantity = input("Enter quantity to update.\t")
                updated_item_set = {item_name: item_quantity}
                user_cart_item.update(updated_item_set)
                for key, value in user_cart_item.items():
                    user_cart_data.write(key + ' : ' + value + '\n')
                print("Your cart has:")
                user_cart_data.seek(0)
                print(user_cart_data.read())

            elif user_activity == 4:
                print("Your cart has:")
                user_cart_data.seek(0)
                print(user_cart_data.read())

            elif user_activity == 5:
                user_activity_status = False
                user_cart_data.close()

            elif user_activity == 6:
                user_cart_data.close()
                acknowledgment = user_delete_request(user_name,user_password)
                if acknowledgment:
                    print(f"{user_name} Account deleted!")
                    break
                else:
                    print("Couldn't perform action. Try again!\n")
            else:
                continue
    except Exception as e:
        print(e)


def user_registration():
    user_name = str(input("Please Enter user user name: \t"))
    user_password = input("Please Enter password:\t")
    if os.path.exists(f'{user_name}.txt'):
        print(f'{user_name} is already registered, Please login!!')
        return False
    else:
        user_registration_data = open(f'{user_name}.txt', 'w')
        # user_credential = {user_name: user_password}
        user_registration_data.write(user_password)
        user_registration_data.close()
        return True


def user_login():
    user_name = input("Please enter user name:\t")
    user_password = input("Please enter password:\t")
    # find_user = f"'{user_name}': '{user_password}'"
    # find_user = '{'+find_user
    user_name_match = False
    user_password_match = False
    if os.path.exists(f'{user_name}.txt'):
        with open(f'{user_name}.txt','r') as user_credintial:
            user_credintial.seek(0)
            for data in user_credintial:
                if user_password == data:
                    user_name_match = True
                    user_password_match = True
                    break
                else:
                    user_name_match = False
                    user_password_match = False

    if user_password_match and user_name_match:
        print(f"Welcome! {user_name}!")
        user_cart(user_name,user_password)

    else:
        print("Sorry! your credentials are wrong")


if __name__ == "__main__":
    try:

        program_status = True
        user_registration_status = False

        while program_status:

            print("Please select one of below options:")

            user_registration_status = str(input("1.New user or 2.Login \n"))
            user_registration_status = user_registration_status.lower().strip()

            if user_registration_status == '1' or user_registration_status == 'newuser' or user_registration_status == 'new user':
                user_registration()
                if user_registration_status:
                    print("Congratulations!!! Registration successful. Please login by choosing login option.")
                else:
                    print("Sorry!!! something wrong. Please try again.")
            elif user_registration_status == '2' or user_registration_status == 'login':
                user_login()
            else:
                continue

    except Exception as e:
        print(e)
