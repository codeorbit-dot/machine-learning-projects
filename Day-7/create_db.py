import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS ai_training")

print("Database created successfully!")

cursor.close()
connection.close()