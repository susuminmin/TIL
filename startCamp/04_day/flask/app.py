from flask import Flask, render_template, request # requests랑 다름 / 사용자의 요청을 확인할 수 있음 
import requests
app = Flask(__name__) 
# html 페이지로 넘겨주려면 (예. <name> 사용하려면) render_template을 임포트한 뒤에야 가능
# 반드시 app.py 가 실행되고... html은 반드시 templates 폴더 안에 있어야 함 


@app.route('/') # / => route
def index():
    return 'Hello World!!'


@app.route('/greeting/<string:name>') # default가 str임
def greeting(name):
    return render_template('greeting.html', name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')             # /search?q=typora 와 비슷
def pong():
    age = request.args.get('age')
    return f'Pong! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # input 네임이 텍스트이기 때문에
    # Ascill Art API 를 활용해서 사용자의 input 값을 변경한다. 
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)
    

if __name__ == '__main__':
    app.run(debug=True) # 이게 있어야 라이브로 반영됨

# 폰트 리스트 가지고 와서 / random 1개 뽑기!
# 만들어줘 make 라는 요청 / 만들어서 사용자한테 보여줌 