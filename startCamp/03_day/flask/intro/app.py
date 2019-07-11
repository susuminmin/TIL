from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)

@app.route("/") # end point
def hello():
    # return 'Hello ssafy2-2!!!'
    return render_template('index.html')
    # folder 이름은 반드시 templates
    # html 파일은 templates 안에 있어야 함


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
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

# Variable Routing (default는 str type!)
@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', html_name=name) # 옵션


@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return render_template('cube.html', html_num=num, html_result=result) # 옵션 넘겨줌 


@app.route('/lunch/<int:people>')
def lunch(people):
     menu = ['짜장면', '짬뽕', '탕수육', '볶음밥']
    choice = random.choices(menu, k=people)
    return str(choice)


@app.route('/movie')
def movie():
    movies = ['스파이더맨', '알라딘', '기생충', '엔드게임']
    return render_template('movie.html', movies=movies)


app.run(debug=True) # 디버그 모드로 하면 라이브로 바뀜 ㅇㅇ

if __name__ == '__main__':
    app.run(debug=True)
