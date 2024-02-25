from datetime import datetime

now = datetime.now()

formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_date)
print(type(formatted_date))

