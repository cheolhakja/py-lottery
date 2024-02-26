import pymysql
import sys


sys.stdin = open("password.txt")
db_endpoint = sys.stdin.readline().strip()
db_user = sys.stdin.readline().strip()
db_pw = sys.stdin.readline().strip()
db_name = sys.stdin.readline().strip()

conn = pymysql.connect(host=db_endpoint, user=db_user, password=db_pw, database=db_name, port = 3306, use_unicode=True, charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = "select * from buy_time"
        cursor.execute(sql)
        conn.commit()
finally:
    conn.close()

result = cursor.fetchall()

member_names = [ i[1] for i in result]

print(member_names)

#---------- 동아리 부원 이름 목록 출력 ----------
    