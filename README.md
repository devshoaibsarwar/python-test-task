# Dynamic Function Execution Based on JSON Status Attribute

## Description

This project demonstrates dynamic function execution in Python based on a JSON input attribute called "status." The application utilizes a PostgreSQL database to store a configuration table with entries specifying actions to be executed for different statuses. The actions are Python functions that can validate phone numbers and email addresses.

## Requirements

To run this project, you will need the following:

- Python 3.x
- PostgreSQL database
- psycopg2 library for Python (for database connection)
- Git (optional, for cloning the repository)

## Setup Instructions

1. Clone the repository (if you haven't already):
```shell
git clone git@github.com:devshoaibsarwar/python-test-task.git
```

2. Create a virtual environment (recommended but optional):
```shell
python -m venv venv
```

3. Install the required Python packages:
```shell
pip install -r requirements.txt
```

## Usage

To execute functions based on the JSON "status" attribute, run the `main.py` script with a sample input JSON. For example:

```shell
python main.py
```


The script will read the "status" attribute from the input JSON, query the configuration table in the database, and execute the specified Python functions in the order defined by the "order_number" column.

## Project Structure

The project directory structure is as follows:

- `main.py`: Contains the main script for executing functions based on the JSON "status."
- `config/database_config.py`: Handles database configuration and table creation.
- `functions/validation_functions.py`: Contains the validation functions for phone numbers and email addresses.
- `requirements.txt`: Lists the required Python packages.
