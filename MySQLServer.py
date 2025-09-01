import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',                 # Use your MySQL username
        password='Janetwambua@22'    # Use your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        cursor.execute("USE alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        # -----------------------------
        # Create tables
        # -----------------------------

        # Authors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                author_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                birth_date DATE
            )
        """)

        # Books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author_id INT NOT NULL,
                published_date DATE,
                price DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (author_id) REFERENCES authors(author_id)
            )
        """)

        # Customers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                phone VARCHAR(20)
            )
        """)

        # Orders table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                order_date DATE NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)

        # Order details table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_details (
                order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                book_id INT NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            )
        """)

        print("All tables created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
