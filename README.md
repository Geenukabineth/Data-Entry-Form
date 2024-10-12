<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Entry Form with Payment Calculation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }

        .container {
            width: 80%;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        pre {
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
        }

        code {
            background-color: #f1f1f1;
            padding: 2px 5px;
            border-radius: 3px;
        }

        table {
            width: 100%;
            margin: 20px 0;
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #333;
            color: #fff;
        }

        .note {
            background-color: #ffeb3b;
            padding: 10px;
            border-radius: 5px;
        }

        .code-block {
            background-color: #f9f9f9;
            border-left: 4px solid #f39c12;
            padding: 10px;
            font-family: monospace;
        }

        a {
            color: #3498db;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Data Entry Form with Payment Calculation</h1>

        <p>This is a simple <strong>Tkinter-based Data Entry Form</strong> for collecting user information, course selection, payment status, and calculating balances. It allows users to register for courses, make payments, and calculate any remaining balance automatically based on the selected course and registration status.</p>

        <h2>Features</h2>
        <ul>
            <li>User information collection: First Name, Last Name, Age, Nationality, etc.</li>
            <li>Course registration: Choose from a list of available courses.</li>
            <li>Payment system:
                <ul>
                    <li>Track payment status (Paid or Not Paid).</li>
                    <li>Automatically calculate the remaining balance based on the selected course and paid amount.</li>
                    <li>Add an extra Rs. 1000 for users who are not yet registered.</li>
                </ul>
            </li>
            <li>Save the collected data to a <code>.txt</code> file.</li>
            <li>Clear form fields with the click of a button.</li>
            <li>Visual design enhancements with custom colors for buttons and the form.</li>
        </ul>

        <h2>Requirements</h2>
        <p>To run this project, you need the following installed:</p>
        <ul>
            <li><strong>Python 3.x</strong></li>
            <li><strong>Tkinter</strong> (comes pre-installed with Python)</li>
        </ul>

        <h2>Setup and Installation</h2>
        <ol>
            <li>Clone the repository or download the project files:</li>
            <pre><code>git clone https://github.com/your-username/repository-name.git
cd repository-name</code></pre>

            <li>Run the Python script:</li>
            <pre><code>python your_script_name.py</code></pre>
        </ol>

        <h2>Usage</h2>
        <ol>
            <li><strong>User Information</strong>: Enter details such as first name, last name, age, title, and nationality.</li>
            <li><strong>Course Selection</strong>: Select a course from the drop-down menu. The course price will be automatically factored into the balance calculation.</li>
            <li><strong>Registration</strong>: If the user is not yet registered, check the 'Currently Registered' option. If left unchecked, Rs. 1000 will be added to the total payment.</li>
            <li><strong>Payment Details</strong>: Choose whether the payment is made or not and enter the amount paid. The balance will automatically update.</li>
            <li><strong>Save Data</strong>: Click the <em>Save Data</em> button to save all the information into a <code>user_data.txt</code> file.</li>
            <li><strong>Clear Form</strong>: Click the <em>Clear</em> button to reset all fields in the form.</li>
        </ol>

        <h2>Code Explanation</h2>
        <p>The application is divided into the following key sections:</p>
        <ul>
            <li><strong>User Information Frame</strong>: Collects user details such as name, age, nationality, and title.</li>
            <li><strong>Course Information Frame</strong>: Allows users to choose a course and mark their registration status.</li>
            <li><strong>Payment Information Frame</strong>: Handles payment status, the amount paid, and balance calculations.</li>
            <li><strong>Save and Clear Buttons</strong>:
                <ul>
                    <li><strong>Save</strong>: Saves all the collected data into a text file.</li>
                    <li><strong>Clear</strong>: Resets the form fields.</li>
                </ul>
            </li>
        </ul>

        <div class="note">
            <p><strong>Balance Calculation:</strong> The balance is calculated based on the selected course's price, and Rs. 1000 is added if the user has not registered yet. The balance is then updated in real-time as the user inputs the paid amount.</p>
        </div>

        <h2>Example <code>user_data.txt</code> Entry:</h2>
        <div class="code-block">
            <p>First Name: John, Last Name: Doe, Title: Mr., Age: 30, Nationality: Sri Lanka, Registered: Yes, Paid: Paid, Paid Amount: 5000, Balance: 10000.00, Course: Data Science</p>
        </div>

        <h2>Screenshots</h2>
        <table>
            <thead>
                <tr>
                    <th>User Information Form</th>
                    <th>Payment Information Form</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><img src="images/user_info_screenshot.png" alt="User Info Screenshot" width="300"></td>
                    <td><img src="images/payment_info_screenshot.png" alt="Payment Info Screenshot" width="300"></td>
                </tr>
            </tbody>
        </table>

        <h2>Contributions</h2>
        <p>Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.</p>

        <h2>License</h2>
        <p>This project is open-source and available under the <a href="LICENSE">MIT License</a>.</p>
    </div>
</body>

</html>
