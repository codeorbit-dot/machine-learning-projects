import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="ai_training"
)

cursor = conn.cursor()

sql = """
INSERT INTO students(name, course, marks)
VALUES(%s, %s, %s)
"""

values = ("Tarun", "Python", 95)

cursor.execute(sql, values)

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()