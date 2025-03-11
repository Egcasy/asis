from cryptography.fernet import Fernet
import os
import json

# File to store encrypted passwords
PASSWORD_FILE = "passwords.json"
KEY_FILE = "key.key"

# Generate or load encryption key
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt a password
def encrypt_password(password, key):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()

# Decrypt a password
def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()

# Save password
def save_password(service, username, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)

    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}

    passwords[service] = {"username": username, "password": encrypted_password}

    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

    print(f"Password saved for {service}!")

# Retrieve password
def get_password(service):
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords stored yet.")
        return

    with open(PASSWORD_FILE, "r") as file:
        passwords = json.load(file)

    if service in passwords:
        key = load_key()
        decrypted_password = decrypt_password(passwords[service]["password"], key)
        print(f"Service: {service}\nUsername: {passwords[service]['username']}\nPassword: {decrypted_password}")
    else:
        print(f"No password found for {service}.")

# List all stored passwords
def list_services():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords stored yet.")
        return

    with open(PASSWORD_FILE, "r") as file:
        passwords = json.load(file)

    if passwords:
        print("Stored services:")
        for service in passwords:
            print(f"- {service}")
    else:
        print("No passwords found.")

# User interaction
def main():
    while True:
        print("\nPassword Manager")
        print("1. Save Password")
        print("2. Get Password")
        print("3. List Services")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            service = input("Enter service name (e.g., Gmail, Facebook): ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(service, username, password)
        elif choice == "2":
            service = input("Enter service name to retrieve password: ")
            get_password(service)
        elif choice == "3":
            list_services()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
