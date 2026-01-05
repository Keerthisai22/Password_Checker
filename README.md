# Password Strength Checker (Python)

A simple Python program that checks whether a password is strong based on basic security rules.

## Features
- Checks minimum password length
- Validates presence of:
  - At least one uppercase letter
  - At least one digit
  - At least one special character
- Continuously asks until a strong password is entered

## Password Rules
A password is considered **strong** if:
- Length is at least 8 characters
- Contains at least one uppercase letter
- Contains at least one digit
- Contains at least one special character

## Technologies Used
- Python 3

## How to Run
1. Download or clone the repository
2. Run the program:
   python password_strength_checker.py

## Sample Output
Enter the password: Hello123  
Weak password  

Enter the password: Hello@123  
Strong password  

## Concepts Used
- while loop
- Conditional statements
- String methods (`isupper()`, `isdigit()`)
- Boolean flags
- User input handling

## Author
Keerthisai
