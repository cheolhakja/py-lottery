from flask import Flask, render_template, request, redirect
import pymysql
import sys

app = Flask(__name__)

sys.stdin = open("password.txt")
db_endpoint = sys.stdin.readline().strip()
db_user = sys.stdin.readline().strip()
db_pw = sys.stdin.readline().strip()
db_name = sys.stdin.readline().strip()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Get the user input from the form
    username = request.form['username']
    num_1 = int(request.form['dropdown1'])
    num_2 = int(request.form['dropdown2'])
    num_3 = int(request.form['dropdown3'])
    num_4 = int(request.form['dropdown4'])

    if check_duplicate_lottery_numbers([num_1, num_2,num_3,num_4]) == False:
        return redirect('/')
    
    # ---------- 이름이 동아리 부원 목록에 있는지 확인 ----------
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

    if username not in member_names:
        return redirect('/')

    # ------------------------------



    # ---------- 하루에 하나로 구매 제한 ----------
    from datetime import datetime

    now = datetime.now()    

    for i in result:
        if i[1] == username:
            last_time_buy = i[2]
            current_time = now.strftime('%Y-%m-%d %H:%M:%S')

            last_time_buy = last_time_buy[:10]
            current_time = current_time[:10]

            if last_time_buy >= current_time:
                return redirect('/')


    
    # ------------------------------


    # ---------- 구매 ----------
    conn = pymysql.connect(host=db_endpoint,
                                 user=db_user,
                                 password=db_pw,
                                 database=db_name, port = 3306, use_unicode=True, charset='utf8')

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO purchase (member_name, num_1, num_2, num_3, num_4) VALUES (%s, %s, %s, %s, %s)"
            #The mysql-python-connector only support %s
            cursor.execute(sql, (username, num_1, num_2, num_3, num_4,))
            conn.commit()
    finally:
        conn.close()
    
    # ----------
        


    # ---------- 최근 구매 시간 업데이트 ----------
    conn = pymysql.connect(host=db_endpoint, user=db_user, password=db_pw, database=db_name, port = 3306, use_unicode=True, charset='utf8')

    try:
        with conn.cursor() as cursor:
            sql = "UPDATE buy_time SET last_time_buy = %s where member_name = %s"
            cursor.execute(sql, (now.strftime('%Y-%m-%d %H:%M:%S'),username))
            conn.commit()
    finally:
        conn.close()    
    # ----------
        


    return redirect('/')


def check_duplicate_lottery_numbers(numbers):
    return len(set(numbers)) == 4


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

   
