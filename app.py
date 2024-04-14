import mysql.connector
from mysql.connector import Error
from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



#регистрация 
@app.route('/register',methods=['GET','POST'])
def registrer():
    
    try:
        # Подключение к базе данных
        connection = mysql.connector.connect(user="root",
                                             password="root",
                                             host="localhost",
                                             raise_on_warnings= True,
                                             database="bazad")
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Получение данных из формы
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            def register_user(username, password,email):
            # Запрос для добавления данных в базу
                sql = "INSERT INTO users (username,password, email) VALUES (%s, %s, %s)"
                val = (username,password ,email)
                cursor.execute(sql, val)
                connection.commit()
                print("Record inserted successfully into users table")
            register_user(username, email, password)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
    
    return render_template('registration.html')





if __name__ == '__main__':

    app.run()
    
