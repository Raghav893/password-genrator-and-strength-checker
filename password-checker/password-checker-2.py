def check_password(password):
    if len(password) <= 8:
        print("password is too weak")

    if password.isalpha():
        print("password is too weak")

    if password.isdigit():
        print("password is too weak")

    if password.isspace():
        print("password is too weak")   

    if password.islower():
        print("password is too weak")

    if password.isupper():
        print("password is too weak")
    password_rate = 0

    for i in password:
        if i.isupper():
            password_rate += 1
            break

    for i in password:
        if i.islower():
            password_rate += 1
            break

    for i in password:
        if i.isdigit():
            password_rate += 1
            break
            
   
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
                    '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', 
                    '?', '/']
    
    
    for i in password:
        if i in special_chars:
            password_rate += 1
            break
            
    if password_rate == 4:
        return "strong"
    elif password_rate == 3:
        return "moderate"
    elif password_rate == 2:
        return "weak"
    else:
        return "too weak"

def create_password():
    import random
    letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_upper = [letter.upper() for letter in letters_lower]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
                    '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', 
                    '?', '/']

    while True:
        length = int(input("Enter the length of the password (minimum 8 characters): "))
        if length >= 8:
            break
        print("Password length must be at least 8 characters!")

    all_chars = letters_lower + letters_upper + numbers + symbols
    
    while True:
        # Ensure at least one character from each category
        password = random.choice(letters_upper)  # One uppercase
        password += random.choice(letters_lower)  # One lowercase
        password += random.choice(numbers)  # One number
        password += random.choice(symbols)  # One symbol
        
        # Fill the rest with random characters
        remaining_length = length - 4
        password += ''.join(random.choice(all_chars) for _ in range(remaining_length))
        
        # Shuffle the password to make it random
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        strength = check_password(password)
        print(f"Generated password: {password}")
        print(f"Password strength: {strength}")
        
        if strength == "strong":
            break
        print("Generated password is not strong enough, generating another one...")

    return password

def main():
    while True:
        print("\nPassword Generator and Checker Menu:")
        print("1. Generate new password")
        print("2. Check existing password")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            password = create_password()
            print(f"\nYour strong password is: {password}")
        
        elif choice == "2":
            password = input("Enter the password to check: ")
            strength = check_password(password)
            print(f"Password strength: {strength}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


main()
