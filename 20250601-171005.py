import json

filename = "username.json"

def get_stored_username():
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("What is your name? ")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        is_correct = input(f"Are you {username}? (y/n): ").lower()
        if is_correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()