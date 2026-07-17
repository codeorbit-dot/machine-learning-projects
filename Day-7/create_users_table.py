import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="ai_training"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100)
)
""")

conn.commit()

print("Users table created!")

cursor.close()
conn.close()