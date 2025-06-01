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