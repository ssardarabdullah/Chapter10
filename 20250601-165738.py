# 10-4: Guest Book
print("Enter 'q' to quit.")
while True:
    name = input("What is your name? ")
    if name.lower() == 'q':
        break
    print(f"Hello, {name}!")
    with open("guest_book.txt", "a") as file:
        file.write(f"{name} visited.\n")