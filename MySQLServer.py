import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='LeoNduta@2005'
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"❌ Failed to connect or create database: {e}")

finally:
    if cursor:
        cursor.close()
    if conn.is_connected():
        conn.close()