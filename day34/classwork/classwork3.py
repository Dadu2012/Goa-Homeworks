def manual_capitalize(user_str):
    
    user_str[0].upper() + user_str[1:].lower()

user_input = input("შეყვანet ტექსტი: ")


print(manual_capitalize(user_input))