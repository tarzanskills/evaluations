def cart(user_name, user_password):
    try:
        cart_item = {}
        activity = True
        cart_data = open(f'{user_name}_cart.txt', 'a+')
        while activity:
            print("choose for what to do.")
            print("1.Add to cart 2.Delete from cart 3.edit quantity 4.View Cart 5.Logout 6.Delete Account \n")
            user_activity = int(input())
            if user_activity == 1:
                item_name = input("Enter item name: \t")
                item_quantity = input(f"Enter {item_name} quantity:\t ")
                cart_item[item_name] = item_quantity
                for key, value in cart_item.items():
                    cart_data.write(key+' : '+value+'\n')
                print("Your cart has:")
                cart_data.seek(0)
                print(cart_data.read())

            elif user_activity == 2:
                item_name = input("Enter item name to delete:\t")

                if item_name in cart_item.keys():
                    del cart_item[item_name]
                    print(f'{item_name} deleted!')
                    for key, value in cart_item.items():
                        cart_data.write(key + ' : ' + value + '\n')
                else:
                    print("Item not found!")

                print("Your cart has:")
                cart_data.seek(0)
                print(cart_data.read())

            elif user_activity == 3:
                item_name = input("Enter item name to modify.")
                item_quantity = input("Enter quantity to update.")
                updated_item_set = {item_name: item_quantity}
                cart_item.update(updated_item_set)
                for key, value in cart_item.items():
                     cart_data.write(key + ' : ' + value + '\n')
                print("Your cart has:")
                cart_data.seek(0)
                print(cart_data.read())

            elif user_activity == 4:
                print("Your cart has:")
                cart_data.seek(0)
                print(cart_data.read())

            elif user_activity == 5:
                user_activity_status = False
                cart_data.close()

            elif user_activity == 6:
                cart_data.close()
                accept = delete_user(user_name, user_password)
                if accept:
                    print(f"{user_name} Account deleted!")
                    break
                else:
                    print("Couldn't perform action. Try again!\n")
            else:
                continue
    except Exception as e:
        print(e)



