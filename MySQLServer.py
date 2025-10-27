import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        mydb_connection = mysql.connector.connect(
          host = "localhost",
        user = "root",
        password = "McQueen1ncha1n$"
        )

        if mydb_connection.is_connected():
            cursor = mydb_connection.cursor()

            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            mydb_connection.commit()

        print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        if mydb_connection.is_connected():
            cursor.close()
            mydb_connection.close()

if __name__ == "__main__":
    create_database()