def manual_isdigit(user_str):
   
    for char in user_str:
        
        if char not in '0123456789':
            print(False)
 
    print(True) 