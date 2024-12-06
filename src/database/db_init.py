from db import Database

db = Database("access_control.db")

db.connect

db.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Tạo bảng AcLocation
db.execute("""
CREATE TABLE IF NOT EXISTS AcLocation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL,
    mode TEXT DEFAULT 'default',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Tạo bảng AcTime
db.execute("""
CREATE TABLE IF NOT EXISTS AcTime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    location_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES AcLocation (id)
)
""")

# Tạo bảng AcDepartmentTime
db.execute("""
CREATE TABLE IF NOT EXISTS AcDepartmentTime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER,
    department_name TEXT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES AcLocation (id)
)
""")

# Tạo bảng AcUserTime
db.execute("""
CREATE TABLE IF NOT EXISTS AcUserTime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User (id),
    FOREIGN KEY (location_id) REFERENCES AcLocation (id)
)
""")

db.close()
print("Database và các bảng đã được taọ thành công")


