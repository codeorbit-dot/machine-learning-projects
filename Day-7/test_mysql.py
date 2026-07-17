import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="ai_training"
)

print("Connected to ai_training successfully!")

connection.close()