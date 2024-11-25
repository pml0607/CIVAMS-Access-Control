class AuthManager:
    def update_auth_token(self, msg):
        """Lưu và cập nhật token xác thực"""
        auth_token = msg['authenToken']
        # Lưu token vào cơ sở dữ liệu hoặc bộ nhớ
        print(f"Auth token updated: {auth_token}")
