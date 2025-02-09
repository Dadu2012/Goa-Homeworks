sentence = input("შეიტანეთ წინადადება: ")  
substring = input("შეიტანე ქტექსტი: ")  

#
position = sentence.find(substring)

if position != -1:
    print(f"'{substring}' პირველი ადგილი არის ინდექსზე {position}.")
else:
    print(f" '{substring}' არ მოიძებნა.")