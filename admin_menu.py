import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
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


def view_all_user_data():
    query ="select id,username,role from users"
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        result=cursor.fetchall()
        
        if not result:
            print("No data")
        data_tuples=[(row['id'],row['username'],row['role'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))

def insert_new_data():
    # Get user input for new data
    username=input("Enter the username :")
    password=input("Enter the password :")
    role=input("Enter the role :")
    try:
        if conn.is_connected():
            cursor=conn.cursor(dictionary=True)
            create_user_query=f"insert into users(username,password,role) values ('{username}','{password}','{role}')"
            cursor.execute(create_user_query)
            conn.commit()
            print(f"user '{username}' created successfully by admin.")
    except Error as e:
        print(f"Error:{e}")




# # Repeat the process for other datasets: categories, country, and platform
# # Example dataset 2: categories
#     categories_columns = ["categories_id", "categories"]
#     categories_data = [
#         (1, "Nature"),
#         (2, "Travel"),
#     # Add other data...
# ]
#     insert_data("categories", categories_columns, categories_data)

# # Example dataset 3: country
#     country_columns = ["country_id", "country"]
#     country_data = [
#         (1, "USA"),
#         (2, "Canada"),
#     # Add other data...
#     ]

#     insert_data("country", country_columns, country_data)

# # Example dataset 4: platform
#     platform_columns = ["Platform_id", "Platform"]
#     platform_data = [
#         (1, "Twitter"),
#         (2, "Instagram"),
#         # Add other data...
#     ]

#     insert_data("platform", platform_columns, platform_data)

#     db.commit()

#     print("New data added successfully.")

def update_data():
    # Get user input for data to be updated
    data_id = int(input("Enter data_id to update: "))
    
    # Get user input for the new values
    new_username = input("Enter new username: ")
    new_role = input("Enter new role: ")

    # Execute an UPDATE query to modify the specified data in the database
    query = "UPDATE users SET username = %s, role = %s WHERE id = %s"
    try:
        cursor.execute(query, (new_username, new_role, data_id))
        conn.commit()
        print(f"Data with id {data_id} updated successfully.")
    except Exception as e:
        print(f"Error updating data: {e}")
        conn.rollback()
    
    # Execute an UPDATE query to modify the specified data in the database
    # ...

def delete_data():
    # Get user input for data to be deleted
    data_id = int(input("Enter data_id to delete: "))
      # Execute a DELETE query to remove the specified data from the database
    query = "DELETE FROM users WHERE id = %s"
    try:
        cursor.execute(query, (data_id,))
        conn.commit()
        print(f"Data with id {data_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
    # Execute a DELETE query to remove the specified data from the database

# Admin CRUD operations
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. View all user data")
        print("2. Insert new data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_user_data()
        elif choice == "2":
            insert_new_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")