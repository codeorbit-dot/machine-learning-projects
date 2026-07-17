import mysql.connector
import bcrypt

username = input("Choose Username: ")
password = input("Choose Password: ")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="ai_training"
)

cursor = conn.cursor()

# Check if username already exists
cursor.execute(
    "SELECT * FROM users WHERE username = %s",
    (username,)
)

existing_user = cursor.fetchone()

if existing_user:
    print("❌ Username already exists!")

else:
    # Hash password
    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    # Insert user
    cursor.execute(
        "INSERT INTO users(username, password) VALUES(%s, %s)",
        (username, hashed_password.decode())
    )

    conn.commit()

    print("✅ Registration Successful!")

cursor.close()
conn.close()