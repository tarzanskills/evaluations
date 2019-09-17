import os

def user_registry():
    user_name = str(input("Enter username:"))
    user_password = input("Enter password:")
    if os.path.exists(f'{user_name}.txt'):
        print(f'{user_name} is already registered, Please login!!')
        return False
    else:
        user_data= open(f'{user_name}.txt', 'w')
        user_data.write(user_password)
        user_data.close()
        return True

def user_login():
    user_name = input("Please enter user name:\t")
    user_password = input("Please enter password:\t")
    user_name_found = False
    user_password_found = False
    if os.path.exists(f'{user_name}.txt'):
        with open(f'{user_name}.txt','r') as user_credential:
            user_credential.seek(0)
            for data in user_credential:
                if user_password == data:
                    user_name_found = True
                    user_password_found = True
                    break
                else:
                    user_name_found = False
                    user_password_found = False

    if user_password_found and user_name_found:
        print(f"Welcome! {user_name}!")
        cart(user_name,user_password)

    else:
        print("credentials dont match")



