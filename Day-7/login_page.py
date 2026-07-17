import mysql.connector
import bcrypt

username = input("Enter Username: ")
password = input("Enter Password: ")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="ai_training"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT password FROM users WHERE username=%s",
    (username,)
)

result = cursor.fetchone()

if result:
    stored_password = result[0]

    if bcrypt.checkpw(
        password.encode(),
        stored_password.encode()
    ):
        print("✅ Login Successful")
    else:
        print("❌ Incorrect Password")

else:
    print("❌ User Not Found")

cursor.close()
conn.close()