import os

num_of_items = int(input("Enter the no of items "))

list_of_cart = {}

def shopping_cart(num_of_items):

    for i in range(num_of_items):

        name = str(input("Enter the name of items "))
        values = int(input(f"Enter the value of {name} items "))

        list_of_cart[name] = values

        for name,values in list_of_cart.items():
            print(f"{name} {values}")

        # if "name" in list_of_cart:
        #     del list_of_cart["name"]


        total_items=sum(list_of_cart.values())
        print(type(list_of_cart))
        print("initial dictionary = ", list_of_cart)


    print("Your cart is  :", list_of_cart)

    print("total value of the items in cart are  ",total_items)


list_in_string = str(list_of_cart)

print(list_in_string)

print(shopping_cart(num_of_items))

# def check_user():
#     with open('userdata.txt') as file:
#         datafile = file.readlines()


    # for line in datafile:
    #     if i in line:
    #         return True
    # return False

#
# if check_user():
#     print('True')
# else:
#     print('False')




