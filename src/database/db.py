import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

    def execute(self, query, params = ()):
        self.connect()
        self.cursor.execute(query, params)
        self.conn.commit()
    
    def fetchall(self):
        """Lấy tất cả kết quả từ truy vấn."""
        return self.cursor.fetchall()

    def fetchone(self):
        """Lấy một kết quả từ truy vấn."""
        return self.cursor.fetchone()

    def close(self):
        """Đóng kết nối cơ sở dữ liệu."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def access(self, user, department):
        self.excute('''SELECT access_allowed, access_days, start_time, end_time
                    FROM access_control
                    WHERE recognize_id = ? AND department_id = ?
                    ''', (user, department))
        rule = self.fetchone()
        return rule