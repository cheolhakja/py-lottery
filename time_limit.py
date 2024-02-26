result = [(1, "nunez", "2023-12-12 23:11:45"),(2, "salah", "2024-01-01 00:00:00"),(3, "virgil", "2024-01-01 00:00:00"),(4, "robo", "2024-01-01 00:00:00")]

from datetime import datetime

now = datetime.now()

last_time_buy = result[0][2] #"2023-12-12 23:11:45"


print(last_time_buy < now.strftime('%Y-%m-%d %H:%M:%S')) #True
