def main():
    while True:
        password = input("What's the password?: ")
        result = check_password(password)
        if result == "too short":
            print("Your password is too short. Please try again! ")
        elif result == "no uppercase":
            print("Your password must contain at least one uppercase character! ")
        elif result == "no lowercase":
            print("Your password must contain at least one lowercase character! ")
        elif result == "no digit":
            print("Your password must contain a digit ")
        elif result == "no symbol":
            print("Your password must contain a symbol! ")
        elif result == "too repetitive":
            print("Your password is too repetitive! ")
        else:
            print(f"Great! your new password is: {password}")
            break
def check_password(password):
    if len(password) < 8:
        return "too short"
    has_upper = False
    has_digit = False
    has_lower = False
    has_symbol = False
    is_repetitive = False
    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        else:
            has_symbol = True
    for j in range(len(password) - 2):
        if password[j] == password[j + 1] == password[j + 2]:
            is_repetitive = True



    if is_repetitive:
        return "too repetitive"
    if not has_upper:
        return "no uppercase"
    if not has_digit:
        return "no digit"
    if not has_lower:
        return "no lowercase"
    if not has_symbol:
        return "no symbol"
    return "valid"



if __name__ == "__main__":
    main()