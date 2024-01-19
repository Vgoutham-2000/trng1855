import mysql.connector
from mysql.connector import Error
from getpass import getpass
from admin_menu import admin_menu
from user_menu import *
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Goutham@3007',
            database='rev'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def login():
    username=input("Enter the username:")
    password=input("Enter the password:")
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                print(f"Login successful! Welcome, {user[1]} (role: {user[3]})")
                if user[3]=="admin":
                    admin_menu()
                else:
                     user_menu()
            else:
                print("Invalid username or password")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    username_input = input("Enter your username: ")
    password_input = getpass("Enter your password: ")

    login(username_input, password_input)
