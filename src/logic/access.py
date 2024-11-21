from database.db import query_db

def check_access(recognize_id, update_at):
    """Kiểm tra quyền truy cập dựa trên cơ sở dữ liệu."""
    result = query_db(
        "SELECT access FROM access_control WHERE recognize_id=? AND update_at=?",
        (recognize_id, update_at)
    )
    return result and result[0]['access']