# 📱 User Management System (Python + MySQL)

A **console-based User Management Application** built using **Python** and **MySQL**.
This project allows users to **register, login, update details, and delete their account**, with proper separation of backend and frontend logic.

This project is created as a **course completion** to demonstrate Python, database connectivity, and clean code structure.

## 🚀 Features

* User Registration (unique username)
* User Login & Logout
* View user details after login
* Change password
* Change address
* Delete user account
* Menu-driven console interface
* MySQL database integration
* Custom exception handling
* Clean and modular project structure

## 🛠️ Tech Stack

* **Python** 3.0+
* **mysql-connector-python** 
* **VS Code** 
* **MySQL Workbench** 

## 📂 Project Structure

```
UserManagementApp/
│
├── app.py            # Frontend menu logic
├── db_manager.py     # Database operations
├── user.py           # User model & validation
├── exceptions.py     # Custom exceptions
├── config.py         # Database configuration
└── README.md
```

## 🗄️ Database Setup

Create database and table in MySQL:

```sql
CREATE DATABASE user_management;
USE user_management;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    address VARCHAR(255)
);
```

## ⚙️ Configuration

Update **config.py** with your MySQL credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password",
    "database": "user_management"
}
```

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/UserManagementApp.git
cd UserManagementApp
```

### 2️⃣ Install Required Package

```bash
pip install mysql-connector-python
```

### 3️⃣ Start MySQL Server

* Windows → Services → Start **MySQL80**
* OR connect via **MySQL Workbench**

### 4️⃣ Run the Application

```bash
python app.py
```

## 🧪 Sample Menu

```
+----------------------------------+
|      📱 USER MANAGEMENT APP      |
+----------------------------------+
| 1. Login                         |
| 2. Register                      |
| 3. Logout                        |
| 4. Exit                          |
+----------------------------------+
```

## ❗ Error Handling

* Duplicate usernames are not allowed
* Invalid login credentials handled gracefully
* Custom exceptions used for cleaner error handling
* Database and runtime errors are safely caught

## 📌 Learning Outcomes

* Python OOP concepts
* MySQL database integration
* Exception handling
* Modular code structure
* Real-world backend & frontend separation
