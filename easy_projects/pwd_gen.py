import random
import string

def generate_pwd(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation 

    chars = letters
    if numbers:
        chars += digits
    if special_chars:
        chars += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(chars)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

        
    return pwd

def pwd_config():
    pwd_length = ""
    pwd_digits = False
    pwd_special = False

    while True:
        pwd_length = input("How many characters do you want the password to have?: ")
        try:
            pwd_length = int(pwd_length)
            if pwd_length <= 0:
                print("Please insert a number greater than 0!")
                continue
            break
        except ValueError:
            print("Please insert a number")
    
    while True:    
        pwd_digits = input("Do you want the password to have digits?(Y/N): ").lower()
        if pwd_digits in ("yes", "y"):
            pwd_digits = True
            break
        elif pwd_digits in ("no", "n"):
            pwd_digits = False
            break
        
    while True:
        pwd_special = input("Do you want the password to have special characters?(Y/N): ").lower() 
        if pwd_special in ("yes", "y"):
            pwd_special = True
            break
        elif pwd_special in ("no", "n"):
            pwd_special = False
            break

    return pwd_length, pwd_digits, pwd_special


def main():
    pwd_length, pwd_digits, pwd_special = pwd_config()
    pwd = generate_pwd(pwd_length, pwd_digits, pwd_special)
    print(f"Generated password: {pwd}")

if __name__ == "__main__":
    main()