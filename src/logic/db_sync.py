import requests

class DatabaseSync:
    def sync(self, msg):
        """Đồng bộ dữ liệu từ server qua API"""
        url = 'http://10.2.6.2/api/face-terminal-person-sync/pullChanges'
        headers = {'Content-Type': 'application/json'}
        data = {
            "lastPulledAt": msg['updatedAt'],
            "tableName": msg['tableName']
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("Data synced successfully")
        else:
            print("Data sync failed")
