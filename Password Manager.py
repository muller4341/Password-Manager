import json

# Create an empty dictionary to store passwords
passwords = {}

# Function to add a new password
def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")
    passwords[website] = {"username": username, "password": password}
    save_passwords()

# Function to view saved passwords
def view_passwords():
    for website, info in passwords.items():
        print(f"Website: {website}")
        print(f"Username: {info['username']}")
        print(f"Password: {info['password']}")
        print("\n")

# Function to save passwords to a JSON file
def save_passwords():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to load passwords from a JSON file
def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Main program loop
def main():
    global passwords
    passwords = load_passwords()
    
    while True:
        print("Options:")
        print("1. Add a new password")
        print("2. View saved passwords")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
