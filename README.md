# Student Marks Entry System using Python & MySQL

This project is a simple **Student Marks Entry System** built using **Python** and **MySQL**.  
It collects student details and subject marks, validates the input, calculates total marks and percentage, and stores the data in a MySQL database with proper error handling.

## Features
- Takes student details (roll number, name, branch)
- Accepts marks for C, C++, and Python subjects
- Validates marks (0–100 range)
- Calculates total marks and percentage automatically
- Stores records in MySQL database
- Uses try–except for input and database error handling
- Safely closes database connections

## Technologies Used
- Python 3.x
- MySQL
- mysql-connector-python

## Requirements
- Python 3.x installed
- MySQL Server installed
- mysql-connector-python library

Install MySQL connector:
```bash
pip install mysql-connector-python
