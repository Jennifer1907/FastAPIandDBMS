import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb;")
cursor.close()
conn.close()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="testdb"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100)
    )
""")

cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO students (name, age, email) VALUES ('Alice', 21, 'alice@example.com')")
    cursor.execute("INSERT INTO students (name, age, email) VALUES ('Bob', 22, 'bob@example.com')")
    cursor.execute("INSERT INTO students (name, age, email) VALUES ('Jen', 25, 'jen@example.com')")
    conn.commit()


cursor.execute("SELECT * FROM students")
print("Danh sách toàn bộ sinh viên:\n")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\n")


print("Danh sách toàn bộ sinh viên có tuổi từ 18 đến 22:\n")
cursor.execute("SELECT * FROM students WHERE (age>=18) AND (age<=22)")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\n")


cursor.execute("UPDATE students SET email = 'nguyenb@gmail.com' WHERE name = 'Bob'")
conn.commit()
print("Danh sách toàn bộ sinh viên sau khi cập nhập email cho Bob:\n")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\n")


cursor.execute("DELETE FROM students WHERE age > 25")
conn.commit()
print("Danh sách toàn bộ sinh viên sau khi xóa sinh viên có tuổi lớn hơn 25:\n")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\n")


print("Danh sách sinh viên có từ khóa tên 'Anh':")
cursor.execute("SELECT * FROM students WHERE name LIKE '%Anh%'")
rows = cursor.fetchall()
if len(rows) ==0:
    print("Không có sinh viên có tên có từ khóa là 'Anh'")
else:
    for row in rows:
        print(row)
print("\n")


print("Đếm số lượng sinh viên theo từng độ tuổi:")
cursor.execute("SELECT age, COUNT(*) FROM students GROUP BY age")
rows = cursor.fetchall()
for row in rows:
    print(row)
