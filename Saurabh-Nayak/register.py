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

