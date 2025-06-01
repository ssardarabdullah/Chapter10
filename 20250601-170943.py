import json
import os

filename = "favorite_number.json"

def get_favorite_number():
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def ask_and_store_number():
    number = input("What is your favorite number? ")
    with open(filename, "w") as f:
        json.dump(number, f)
    return number

def main():
    number = get_favorite_number()
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = ask_and_store_number()
        print(f"Got it! I'll remember your favorite number: {number}.")

main()