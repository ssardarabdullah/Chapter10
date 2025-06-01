Question 1_______
 Write a program that prompts 
the user for their name.
When theyrespond, write their name to a 
file called guest.txt.

solution _______
Guest
name = input("What is your name? ")
with open("guest.txt", "w") as file:
    file.write(name)
