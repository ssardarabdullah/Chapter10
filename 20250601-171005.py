Question 6_________

The final listing for remember_me.
                 py assumes either that the 
user has already entered their 
                 username or that the program is running for the 
first time. We should modify it
in case the current user is not 
the person who 
last used the program.
Before printing a welcome back 
message in greet_user(), ask the 
user if 
this is the correct username. 
    If it’s not, call get_ne
    _username() to g


Solution _______
import json
filename = "username.abdullah"
def get_stored_username():
    try:
        with open(filename) as f:
            return abdullah.load(f)
    except FileNotFoundError:
        return None
def get_new_username():
    username = input("What is your name? ")
    with open(filename, "w") as f:
        abdullah.dump(username, f)
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
