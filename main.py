import mysql.connector
import csv
from mysql.connector import Error
from register import *
from login import *

# from menu_1 import MainMenu

# Replace these values with your MySQL server information
host = "localhost"
user = "root"
password = "Goutham@3007"
database="rev"

conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

cursor = conn.cursor()

# def load_data_from_csv(conn, csv_path, table_name):
     
#     with open(csv_path, 'r', encoding='utf-8', errors='replace') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             placeholders = ', '.join(['%s' for _ in row])
#             query = f'INSERT INTO {table_name} VALUES ({placeholders})'
#             print(f"Executing query: {query}")
#             print(f"Number of columns in row: {len(row)}")
#             cursor.execute(query, row)
#     conn.commit()
#     print(f"Data loaded into '{table_name}' table successfully.")


# # Your existing code...

# # Establish a connection
# try:
#     conn = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

#     if conn.is_connected():
#         print("Connected to MySQL server")

#         # Uncomment the following section to create tables if needed
#         cursor = conn.cursor()
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS main_table (
#         data_id INT PRIMARY KEY,
#         Text TEXT,
#         Platform_id INT,
#         Sentiment_id INT,
#         Categories_id INT,
#         Country_id INT,
#         Retweets INT,
#         Likes INT,
#         Year INT,
#         Month INT,
#         Day INT,
#         Hour INT
# );

#      """)

#         # Create other tables if needed...

#         # Uncomment the following lines to create categories, platform, and country tables if needed
#         # cursor.execute("""
#         # CREATE TABLE IF NOT EXISTS categories (
#         #     categories_id INT AUTO_INCREMENT PRIMARY KEY,
#         #     categories VARCHAR(255) NOT NULL
#         # );
#         # """)

#         # cursor.execute("""
#         # CREATE TABLE IF NOT EXISTS platform (
#         #     Platform_id INT AUTO_INCREMENT PRIMARY KEY,
#         #     Platform VARCHAR(255) NOT NULL
#         # );
#         # """)

#         # cursor.execute("""
#         # CREATE TABLE IF NOT EXISTS country (
#         #     Country_id INT AUTO_INCREMENT PRIMARY KEY,
#         #     Country VARCHAR(255) NOT NULL
#         # );
#         # """)
#         load_data_from_csv(conn, 'C:/Users/User/hello2/trng1855/csv/main_table.csv', 'main_table')
#         conn.commit()
# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL server: {e}")

# finally:
#     # Close the connection when done
#     if 'connection' in locals() and conn.is_connected():
#         conn.commit()
#         conn.close()
#         print("Connection closed")




def main():
    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
  
  

