import csv
import sys
from password_checker import check_password


def new_user_validation(username):

    if len(username) < 8 or len(username) > 16:
        return "invalid length"
    letter_count = 0
    for j in username:
        if j.isalpha():
            letter_count += 1
        else:
            pass
    if letter_count < 4:
        return "invalid alpha"

    for i in username:
        if i.isspace():
            return "contains space"

    return "valid"



def attempts(atts):
    result = 4 - atts
    if result > 1:
        print(f"{result} attempts remaining! ")
    elif result == 1:
        print(f"{result} attempt remaining! ")
    else:
        print("You have been banned! "), sys.exit()




def get_choice():
    i = 0
    while True:
        print("1. Register\n"
              "2. Log in\n"
              "3. Quit")
        choice = input("Please enter your choice: (1, 2, 3): ").strip()
        if choice not in ["1", "2", "3"]:
            print("Please enter a valid number")
            attempts(i)
            i += 1
            continue
        else:
            if choice == "1":
                print("---------Welcome!----------")
                print("-----------Rules-----------\n"
                      "Your username should be more than 8 and less than 16 characters long\n"
                      "Your username must contain at least 4 alphabetical characters\n"
                      "Your username must not contain spaces")

                new_username = input("Please choose your username!: ")
                y = 0
                while True:
                    result = new_user_validation(new_username)
                    if result == "invalid length":
                        print("Your username should be more than 8 and less than 16 characters long!")
                    elif result == "invalid alpha":
                        print("Your username must contain at least 4 alphabetical characters!")
                    elif result == "contains space":
                        print("Your username cannot contain spaces!")
                    else:
                            taken = False
                            with open("users.csv", newline="") as File:
                                reader = csv.DictReader(File)
                                for user in reader:
                                    if user["username"] == new_username:
                                        taken = True
                            if taken:
                                print("Sorry, that username is already taken! Please choose another one!")
                                attempts(y)
                                y += 1
                                new_username = input("Please choose your username!: ")
                                continue
                            else:
                                print(f"Hello, {new_username}! ")
                                break
                    attempts(y)
                    y += 1
                    new_username = input("Please choose your username!: ")

                print("---------Create a password-----------")
                print("---------------RULES-----------------")
                print("Your password must contain an uppercase letter\n"
                      "Your password must contain a lowercase letter\n"
                      "Your password must contain digits\n"
                      "Your password must not be too repetitive\n"
                      "Your password must contain a symbol(#, $, @, !, etc...)")
                k = 0
                while True:
                    new_password = input(f"Choose a password for {new_username}: ")
                    result = check_password(new_password)
                    if result == "too short":
                        print("Your password is too short")
                    elif result == "too repetitive":
                        print("Your password is too repetitive!")
                    elif result == "no symbol":
                        print("Your password must contain symbols! (#, $, @, !, etc...)")
                    elif result == "no lowercase":
                        print("Your password must contain a lowercase letter!")
                    elif result == "no uppercase":
                        print("Your password must contain an uppercase letter!")
                    elif result == "no digit":
                        print("Your password must contain a digit!")
                    else:
                        print(f"Great! Your password is: {new_password}")
                        with open("users.csv", "a", newline="") as file:
                            fieldnames = ["username", "password"]
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writerow({"username": new_username, "password": new_password})
                        break

                    attempts(k)
                    k += 1

            elif choice == "2":
                b = 0
                while True:
                    username = input("What is your username?: ")
                    found_user = None
                    found_password = None
                    with open("users.csv") as file0:
                        for line in file0:
                            user, password = line.rstrip().split(",")
                            if user == username:
                                found_user = user
                                found_password = password
                        if not found_user:
                            if b != 4:
                                print("Sorry, we could not find you username. Try again")
                            attempts(b)
                            b += 1
                            continue
                        else:
                            c = 0
                            while True:
                                password = input("Please enter your password: ")
                                if password == found_password:
                                    print(f"Welcome {user}!")
                                    sys.exit()
                                else:
                                    print("Incorrect password")
                                    attempts(c)
                                    c += 1
                                    continue


            elif choice == "3":
                print("It was nice assisting you! Goodbye! ")
                sys.exit()
if __name__ == "__main__":
    get_choice()