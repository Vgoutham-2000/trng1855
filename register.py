import mysql.connector
from mysql.connector import Error
from getpass import getpass

def create_connection():    
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Goutham@3007',
            database='rev'
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def register():
    username=input("Enter the username:")
    password=input("Enter the password:")
    role=input("Enter the role :")
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password, role))
            conn.commit()
            print("Registration successful!")
            #login(username,password)

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def login():
    username=input("Enter the username:")
    password=input("Enter the password:")
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                print(f"Login successful! Welcome, {user[1]} (Role: {user[3]})")
            else:
                print("Invalid username or password")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()

if __name__=="__main__":
    username=input("Enter the username :")
    password=input("Enter the password :")
    role=input("Enter the role (user/admin) :")
    register(username,password,role)
