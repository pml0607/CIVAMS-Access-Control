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

    def execute(self, query, params = None):
        self.connect()
        if params == None:
            self.cursor.execute(query)
        else:
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
        self.execute('''SELECT
                            at.start_time,
                            at.end_time,
                            
                        FROM
                            User u
                        JOIN
                            AcUserTime ut ON u.id = ut.user_id
                        JOIN
                            AcLocation loc ON ut.location_id = loc.id
                        JOIN
                            AcDepartmentTime d ON loc.id = d.location_id
                        JOIN
                            AcTime at ON loc.id = at.location_id
                        WHERE
                            ut.user_id = ?  -- ID của người dùng cần kiểm tra
                            AND ut.location_id = ?  -- ID của department cần kiểm tra
                            

                    ''', (user, department))
        rule = self.fetchone()
        return rule
