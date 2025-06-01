Question 2 ______
Write a while loop that prompts
users for their name. When
they enter their name, print a
greeting to the screen and add a
line recordingtheir visit in a file called
guest_book.txt. Make sure each
entry appears on anew line in the file.


solution _______
Guest Book
print("Enter 'q' to quit.")
while True:
    name = input("What is your name? ")
    if name.lower() == 'q':
        break
    print(f"Hello, {name}!")
    with open("guest_book.txt", "a") as file:
        file.write(f"{name} visited.\n")
