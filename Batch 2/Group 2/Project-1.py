import random
import string

def is_weak_password(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    user_input = input("Enter a password: ")

    if is_weak_password(user_input):
        print("Weak password. Generating a new one...")
        new_password = generate_password()
        print("New password:", new_password)
    else:
        print("Strong password.")


main()