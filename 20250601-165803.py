Question 3_____
Write a while loop that asks
people why they like
programming. Each time someone
enters a reason, add their
reason to a filethat stores all the responses.


solution ______
 Programming Poll
print("Enter 'q' to quit.")
while True:
    reason = input("Why do you like programming? ")
    if reason.lower() == 'q':
        break
    with open("programming_poll.txt", "a") as file:
        file.write(f"{reason}\n")
