import os
def delete_user(user_name, user_password):
    if os.path.exists(f'{user_name}.txt'):
        os.remove(f'{user_name}.txt')
        os.remove(f'{user_name}_cart.txt')
        return True
    else:
        return False
