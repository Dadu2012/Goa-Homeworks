sentence = "I love programming with Python. Python is amazing!"
position = sentence.find("Python")

if position != -1:
    print(f"The first occurrence of 'Python' is at index {position}.")
else:
    print("The word 'Python' was not found.")