# Data Entry Form with Payment Calculation

This is a simple **Tkinter-based Data Entry Form** that allows users to enter personal details, register for courses, and calculate payments. It features automatic balance calculation based on registration status and the amount paid, along with saving data to a file.

## Features

- **User Information Collection**: First Name, Last Name, Age, Nationality, etc.
- **Course Registration**: Select from a list of available courses.
- **Payment Calculation**:
  - Track payment status (Paid or Not Paid).
  - Automatically calculate the remaining balance based on the selected course and amount paid.
  - Add Rs. 1000 to the payment if registration is not completed.
- **Save Data**: Store all collected data in a text file.
- **Clear Form**: Reset all form fields easily.
- **User-Friendly Interface**: Colored buttons and clean design for better usability.

## Requirements

To run this project, you need the following:

- **Python 3.x**
- **Tkinter** (included with Python)

## Setup and Installation

1. Clone the repository or download the project files:
    ```bash
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

2. Run the Python script:
    ```bash
    python data_entry_form.py
    ```

## Usage

1. **Enter User Information**: Provide first name, last name, age, nationality, and title.
2. **Select a Course**: Choose a course from the dropdown list.
3. **Registration Status**: Check or uncheck the "Currently Registered" option. Rs. 1000 will be added to the balance if not registered.
4. **Payment Details**: Choose if the payment is made, enter the amount paid, and the balance will update automatically.
5. **Save Data**: Click the "Save Data" button to save all the information into a `user_data.txt` file.
6. **Clear Form**: Click the "Clear" button to reset all fields.

## Code Overview

The application consists of three main sections:

1. **User Information Frame**: Collects user details like name, age, nationality, and title.
2. **Course Information Frame**: Handles course selection and registration status.
3. **Payment Information Frame**: Includes payment status, paid amount, and balance calculation.

### Balance Calculation Logic
- The balance is calculated based on a course fee of Rs. 10,000.
- If the user is not registered, Rs. 1000 is added to the total fee.
- The balance is then computed by subtracting the paid amount from the total fee.

## Example `user_data.txt` Output

```plaintext
First Name: John, Last Name: Doe, Title: Mr., Age: 30, Nationality: Sri Lanka, Registered: Yes, Paid: Paid, Paid Amount: 5000, Balance: 5000.00, Course: Data Science

Screenshots
