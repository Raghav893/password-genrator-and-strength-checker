#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string check_password(const string& password) {
    if (password.length() <= 8) {
        return "too weak";
    }

    bool has_upper = false, has_lower = false, has_digit = false, has_special = false;
    string special_chars = "!@#$%^&*()-_+={}[]|\\:;\"'<>,.?/";

    for (char c : password) {
        if (isupper(c)) has_upper = true;
        if (islower(c)) has_lower = true;
        if (isdigit(c)) has_digit = true;
        if (special_chars.find(c) != string::npos) has_special = true;
    }

    int password_rate = has_upper + has_lower + has_digit + has_special;

    if (password_rate == 4) return "strong";
    else if (password_rate == 3) return "moderate";
    else if (password_rate == 2) return "weak";
    else return "too weak";
}

string create_password() {
    string letters_lower = "abcdefghijklmnopqrstuvwxyz";
    string letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string numbers = "0123456789";
    string symbols = "!@#$%^&*()-_+={}[]|\\:;\"'<>,.?/";

    int length;
    while (true) {
        cout << "Enter the length of the password (minimum 8 characters): ";
        cin >> length;
        if (length >= 8) break;
        cout << "Password length must be at least 8 characters!" << endl;
    }

    srand(time(0));

    while (true) {
        string password;
        
        password += letters_upper[rand() % letters_upper.size()];
        password += letters_lower[rand() % letters_lower.size()];
        password += numbers[rand() % numbers.size()];
        password += symbols[rand() % symbols.size()];

        string all_chars = letters_lower + letters_upper + numbers + symbols;

        for (int i = 4; i < length; i++) {
            password += all_chars[rand() % all_chars.size()];
        }

        random_shuffle(password.begin(), password.end());

        string strength = check_password(password);
        cout << "Generated password: " << password << endl;
        cout << "Password strength: " << strength << endl;

        if (strength == "strong") {
            return password;
        }
        cout << "Generated password is not strong enough, generating another one..." << endl;
    }
}

int main() {
    while (true) {
        cout << "\nPassword Generator and Checker Menu:" << endl;
        cout << "1. Generate new password" << endl;
        cout << "2. Check existing password" << endl;
        cout << "3. Exit" << endl;

        string choice;
        cout << "Enter your choice (1-3): ";
        cin >> choice;

        if (choice == "1") {
            string password = create_password();
            cout << "\nYour strong password is: " << password << endl;
        }
        else if (choice == "2") {
            string password;
            cout << "Enter the password to check: ";
            cin >> password;
            string strength = check_password(password);
            cout << "Password strength: " << strength << endl;
        }
        else if (choice == "3") {
            cout << "Goodbye!" << endl;
            break;
        }
        else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
} 