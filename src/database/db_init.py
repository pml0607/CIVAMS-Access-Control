from db import Database

db = Database("access_control.db")

db.connect

db.execute("""CREATE TABLE IF NOT EXISTS User (
    id TEXT PRIMARY KEY,
    roleId TEXT,
    name TEXT,
    birthday TEXT,
    gender INTEGER,
    companyId TEXT,
    departmentId TEXT,
    phone TEXT,
    activeStatus INTEGER,
    dateCreated TEXT,
    dateModified TEXT
);""")

db.execute("""
CREATE TABLE IF NOT EXISTS Company (
    id TEXT PRIMARY KEY,
    name TEXT,
    isActive INTEGER,
    dateCreated TEXT,
    dateModified TEXT
);
""")
db.execute("""
CREATE TABLE IF NOT EXISTS Department (
    id TEXT PRIMARY KEY,
    name TEXT,
    companyId TEXT,
    isActive INTEGER,
    dateCreated TEXT,
    dateModified TEXT
);""")

db.execute("""
CREATE TABLE IF NOT EXISTS AcLocation (
    id TEXT PRIMARY KEY,
    name TEXT,
    status TEXT,
    isAlwayOpen INTEGER,
    dateCreated TEXT,
    dateModified TEXT
);""")

db.execute("""
CREATE TABLE IF NOT EXISTS AcTime (
    id TEXT PRIMARY KEY,
    name TEXT,
    startDate TEXT,
    endDate TEXT,
    startHour INTEGER,
    startMin INTEGER,
    startSec INTEGER,
    endHour INTEGER,
    endMin INTEGER,
    endSec INTEGER,
    weekDays TEXT,
    status TEXT,
    dateCreated TEXT,
    dateModified TEXT
);""")

db.execute("""
CREATE TABLE IF NOT EXISTS AcDepartmentTime (
    acLocationId TEXT,
    departmentId TEXT,
    acTimeId TEXT,
    status TEXT,
    dateCreated TEXT,
    dateModified TEXT,
    PRIMARY KEY (acLocationId, departmentId, acTimeId)
);
""")
db.execute("""
CREATE TABLE IF NOT EXISTS AcUserTime (
    acLocationId TEXT,
    userId TEXT,
    acTimeId TEXT,
    status TEXT,
    dateCreated TEXT,
    dateModified TEXT,
    PRIMARY KEY (acLocationId, userId, acTimeId)
);""")

db.close()
print("Database và các bảng đã được taọ thành công")


