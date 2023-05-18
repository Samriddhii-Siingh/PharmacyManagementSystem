# Pharmacy Management System

The Pharmacy Management System is a simple and efficient solution for managing medicine information and automating various pharmacy management tasks. It includes a Python script for interacting with the pharmacy database and a sample database file with pre-populated data.

## Features

- View the list of medicines in the pharmacy
- Add new medicines to the inventory
- Update the quantity and other details of existing medicines
- Delete medicines from the inventory

## Prerequisites

To run the Pharmacy Management System, you need to have the following software installed on your system:

- Python 3: [Download Python](https://www.python.org/downloads/)
- MySQL Server: [Download MySQL](https://dev.mysql.com/downloads/)
- phpMyAdmin (optional): [Download phpMyAdmin](https://www.phpmyadmin.net/downloads/)

## Installation

1. Clone this repository to your local machine or download the source code as a ZIP file.
2. Make sure you have a MySQL server installed and running on your system.
3. If you prefer to use phpMyAdmin for managing the database, install and configure it according to the official documentation.
4. Create a new database in your MySQL server for the pharmacy management system.
5. Import the provided sample database file (`database.txt`) into the newly created database.
   - If you are using phpMyAdmin, you can import the file through the web interface.
   - If you prefer the command line, use the following command: `mysql -u <username> -p <database_name> < database.txt`
6. Install the required Python packages by running the following command in the project directory:

   ```bash
   pip install -r requirements.txt
   
## Usage

1. Make sure that the MySQL server and the database are running.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the pharmacy management system:

   python project.py
   
4. Feel free to explore and adapt the queries according to your requirements.

## Database Structure

The sample database file (`database.txt`) contains a table named `medicines_info` that represents the structure of the pharmacy database. The table includes the following columns:

- `Med_code`: An integer representing the unique identifier for each medicine.
- `Med_name`: A varchar field holding the name of the medicine (up to 30 characters).
- `Qty`: An integer representing the quantity of the medicine available.
- `MRP`: A double (floating-point) field representing the maximum retail price of the medicine.
- `Mfg`: A date field indicating the manufacturing date of the medicine.
- `Exp`: A date field indicating the expiration date of the medicine.
- `Purpose`: A varchar field describing the purpose or usage of the medicine (up to 30 characters).

## Getting Started

To use this pharmacy database, you need to have a MySQL server and phpMyAdmin installed on your system. Follow these steps to get started:

1. Download and install a MySQL server on your machine.
2. Install phpMyAdmin to manage the MySQL server.
3. Create a new database named `pharmacy` in phpMyAdmin.
4. Open phpMyAdmin and import the provided SQL dump file (`pharmacy.sql`).
5. The `medicines_info` table and sample data will be imported into the `pharmacy` database.


## Contributing

Contributions to the Pharmacy Management System are welcome. If you find any issues, have suggestions for improvements, or would like to add new features, please submit a pull request or open an issue on the repository.

## License

This project is licensed under the MIT License.
