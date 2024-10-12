# Data Entry Form with Payment Calculation

This is a simple **Tkinter-based Data Entry Form** that allows users to enter personal details, register for courses, and calculate payments. The form features automatic balance calculation based on registration status and the amount paid, along with the option to save the data to a file.

## Features

- **User Information Collection**: Enter personal details like First Name, Last Name, Age, Nationality, and Title.
- **Course Registration**: Select a course from the available options.
- **Payment Calculation**:
  - Track payment status (Paid or Not Paid).
  - Automatically calculate the balance based on the course selected and amount paid.
  - Add Rs. 1000 to the payment if the registration is not completed.
- **Save Data**: Save all the data into a `user_data.txt` file.
- **Clear Form**: Reset all form fields with a clear button.
- **User-Friendly Interface**: The interface is designed with colored buttons and a simple layout for easy navigation.

## Requirements

To run this project, you need:

- **Python 3.x**
- **Tkinter** (usually included with Python)

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

1. **Enter User Information**: Fill in details like first name, last name, age, nationality, and title.
2. **Select a Course**: Choose a course from the dropdown list.
3. **Registration Status**: Check or uncheck the "Currently Registered" option. Rs. 1000 will be added to the balance if registration is not completed.
4. **Payment Details**: Select if payment is made, enter the amount paid, and the balance will update automatically.
5. **Save Data**: Click the "Save Data" button to save the entered information to a `user_data.txt` file.
6. **Clear Form**: Click the "Clear" button to reset all fields.

## Code Overview

The application consists of three main sections:

1. **User Information Frame**: Gathers user details like name, age, nationality, and title.
2. **Course Information Frame**: Manages course selection and registration status.
3. **Payment Information Frame**: Tracks payment status, paid amount, and balance calculation.

### Balance Calculation Logic
- The base course fee is Rs. 10,000.
- If the user is not registered, an additional Rs. 1000 is added to the total fee.
- The balance is calculated by subtracting the paid amount from the total fee.

## Screenshots

### User Information Form
![User Information Form](screenshots/Screenshot 2024-10-12 235351.png)



## Example `user_data.txt` Output

```plaintext
First Name: John, Last Name: Doe, Title: Mr., Age: 30, Nationality: Sri Lanka, Registered: Yes, Paid: Paid, Paid Amount: 5000, Balance: 5000.00, Course: Data Science
