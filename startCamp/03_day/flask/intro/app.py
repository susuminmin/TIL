from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello ssafy2-2!!!'

@app.route('/ssafy')
def ssafy():
    return 'Hello SSAFY'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 8, 23)
    td = b_day - today
    return f'{td.days} 일 남았습니다!'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_lines')
def html_lines():
    return'''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

# Variable Routing (default는 str type!)
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/cube/<int:num>')
def cube(num):
    return f'{num}의 3 제곱은 {num ** 3} 입니다.'


# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '탕수육', '볶음밥']
    choice = random.choices(menu, k=people)
    return str(choice)
    

app.run(debug=True) # 디버그 모드로 하면 라이브 ㅇㅇ

if __name__ == '__main__':
    app.run(debug=True)