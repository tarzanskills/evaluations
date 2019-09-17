file=open('i.txt','a')
count = 0
while True:
    userName = input("Hello! Welcome! \n\nUsername: ")
    password = input("Password: ")
    count += 1
    if count == 3:
        break
    else:
        if userName == 'Saneeya' and password == '1234':
            break
        else:
            print("Incorrect Password")
file.close()