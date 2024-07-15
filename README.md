# Personal Accounting Application

## Description

This is a small personal accounting application built with Django and SQLite. It allows users to manage their financial accounts, record transactions (both income and expense), categorize transactions, and generate reports based on custom date ranges.

**Note:** This is my first project using Django and is intended for practice purposes only.

## Features

- Add financial accounts.
- Add and delete transactions.
- Categorize transactions.
- Generate financial reports for custom date ranges.
- Calculate and display total income, total expenses, and balance on the homepage.
- Responsive design using Bootstrap.

## Installation

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/mhk2012/personal_accounting.git
    cd personal_accounting
    ```

2. Create a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

5. (Optional) Create a superuser to access the Django admin:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

### Adding Financial Accounts

1. Navigate to the "Add Financial Account" page.
2. Fill in the account name. If it is a bank account, also provide the bank name and account number.
3. If it is a cash account, check the "Is Cash" checkbox.
4. Click the "Save" button to add the account.

### Adding Transactions

1. Navigate to the "Add Transaction" page.
2. Select a category, financial account, and transaction type (Income or Expense).
3. Enter the amount and date of the transaction.
4. Click the "Save" button to add the transaction.

### Generating Reports

1. Navigate to the "Generate Report" page.
2. Select the start and end dates for the report.
3. Click the "Generate" button to view the report.
4. The report will display the total income, total expenses, balance, and a detailed list of transactions within the selected date range.

## Project Structure

```plaintext
personal_accounting/
│
├── accounting/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_financial_account.html
│   │   ├── add_transaction.html
│   │   ├── index.html
│   │   ├── report.html
│   │   ├── report_results.html
│   │   └── base.html
│   ├── templatetags/
│   │   ├── __init__.py
│   │   ├── form_helpers.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── personal_accounting/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the Apache License.
