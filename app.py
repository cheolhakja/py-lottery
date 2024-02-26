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

    conn = pymysql.connect(host=db_endpoint,
                                 user=db_user,
                                 password=db_pw,
                                 database=db_name, port = 3306, use_unicode=True, charset='utf8')

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO purchase (name, num_1, num_2, num_3, num_4) VALUES (%s, %s, %s, %s, %s)"
            #The mysql-python-connector only support %s
            cursor.execute(sql, (username, num_1, num_2, num_3, num_4,))
            conn.commit()
    finally:
        conn.close()
    
    return redirect('/')


def check_duplicate_lottery_numbers(numbers):
    return len(set(numbers)) == 4


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

   
