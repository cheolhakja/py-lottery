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
    num_1 = request.form['dropdown1']
    num_2 = request.form['dropdown2']
    num_3 = request.form['dropdown3']
    num_4 = request.form['dropdown4']


    # Connect to the database
    '''conn = pymysql.connect(host=db_endpoint,
                                 user=db_user,
                                 password=db_pw,
                                 database=db_name, port = 3306, use_unicode=True, charset='utf8')

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (username) VALUES (%s)"
            cursor.execute(sql, (username,))
            conn.commit()
    finally:
        # Close the database connection
        conn.close()'''
    
    print(username)
    print(num_1, num_2, num_3, num_4)

    # Redirect the user back to the home page
    return redirect('/')

if __name__ == '__main__':

    
   
    app.run(debug=True)

   
