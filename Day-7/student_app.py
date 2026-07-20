import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="ai_training"
)

cursor = conn.cursor()

name = input("Enter Student Name: ")
course = input("Enter Course: ")
marks = int(input("Enter Marks: "))

sql = """
INSERT INTO students(name, course, marks)
VALUES(%s, %s, %s)
"""

cursor.execute(sql, (name, course, marks))
conn.commit()

print("✅ Student Added Successfully")

cursor.close()
conn.close()