correct_pass = "Goa best"
count = 0
user_pass = input("Enter password: ")

while user_pass != correct_pass:
    count += 1
    user_pass = input("Enter password: ")

print("Correct password")
print("You needed " + str(count) + " tries!")