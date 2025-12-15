import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="user_management",
        port=3306
    )
    print("✅ MySQL connection established")
except Exception as e:
    print("❌ Connection failed:", e)
