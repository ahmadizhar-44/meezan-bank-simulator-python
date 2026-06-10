# Python Banking System

A simple console-based Banking Management System developed in Python. This project demonstrates the use of functions, conditional statements, loops, exception handling, and basic account management operations.

## Features

- Create a new bank account
- Check account balance
- Deposit money
- Withdraw money
- Input validation using exception handling
- Prevents invalid transactions
- User-friendly menu-driven interface

## Technologies Used

- Python 3

## Project Workflow

1. User creates a bank account.
2. Initial balance is set to zero.
3. User can:
   - Check Balance
   - Deposit Money
   - Withdraw Money
4. The system validates all inputs.
5. Program continues until the user chooses Exit.

## Functions Used

### create_account()
Creates a new bank account and initializes balance.

### check_balance()
Displays account holder name and current balance.

### Deposite()
Allows users to deposit money after validation.

### Withdraw()
Allows users to withdraw money while checking sufficient balance.

## Exception Handling

The project handles invalid user inputs using:

```python
try:
    choice = int(input())
except ValueError:
    print("Enter valid digits only")
```

This prevents program crashes caused by non-numeric inputs.

## Learning Objectives

This project was built to practice:

- Python Functions
- Variables
- Conditional Statements
- Loops
- Exception Handling
- User Input Validation
- Basic Banking Logic

## Sample Output

```text
Welcome to the Meezan Bank

1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit

Enter your choice: 1
Enter your name: Ahmad

Your account was created successfully
```

## Future Improvements

- Multiple account support
- Account number generation
- PIN authentication
- Transaction history
- Data storage using files
- Database integration (MySQL)
- Graphical User Interface (Tkinter)

## Author

Ahmad

Machine Learning & AI Enthusiast
