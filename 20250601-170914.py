Question 4_________

 Write a program that prompts
     for the user’s favorite
number. Use json.dump() to store 
this number in a file. Write a
separate pro￾gram that reads in 
this value and prints the message,
“I know your favorite number!


Solution __________
import json
number = input("What is your favorite number? ")
with open("favorite_number.json", "w") as f:
    json.dump(number, f)
    import json
try:
    with open("favorite_number.json") as f:
        number = json.load(f)
        print(f"I know your favorite number! It's {number}.")
except FileNotFoundError:
    print("Favorite number file not found.")
