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
    age = request.args.get('age') # 화면에 빈칸?!
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
    






###### 로또 실습 ######

# 사용자가 input 입력할 수 있게 페이지만 전달하는 route 
@app.route('/lotto_input')
def lotto_input():
    # 사용자가 입력할 수 있는 페이지만 전달
    return render_template('lotto_input.html')
    
# 폰트 리스트 가지고 와서 / random 1개 뽑기!
# 만들어줘 make 라는 요청 / 만들어서 사용자한테 보여줌 


@app.route('/lotto_result') # 제출하면 이쪽으로 와
def lotto_result():
    # 사용자 입력 값 받기 
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split()

    # 로또 실제 당첨번호 확인
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # Json 타입의 파일을 python dictionary 로 parsing 해줘
    winner = []
    for i in range(1, 7):
        winner.append(str(lotto_info[f'drwtNo{i}']))

    # print(lotto_numbers) # 사용자 도전 번호
    # print(winner) # 실제 당첨번호


    # 번호 교집합 개수 찾기
    if len(lotto_numbers) == 6:         # 사용자 숫자가 딱 6개가 맞는지 확인!
        matched = 0
        for number in lotto_numbers:    # 사용자 숫자를 하나씩 확인하면서 
            if number in winner:        # 당첨번호에 있는지 체크해서
                matched += 1            # 당첨시 matched 를 1씩 증가시킨다.    

        if matched == 6:
            result = '1등입니다!'
        elif matched == 5:              # 보너스 넘버..!
            if lotto_info['bnusNo'] in lotto_numbers:
                result = '2등입니다!'
            else:
                result = '3등입니다!'
        elif matched == 4:
            result = '4등입니다.'
        elif matched == 3:
            result = '5등입니다...'
        else:
            result = '꽝입니다........8ㅅ8'
    else:
        result = '입력하신 숫자가 6개가 아닙니다.'
        
    return render_template('lotto_result.html', result=result)

    



if __name__ == '__main__':
    app.run(debug=True) # 이게 있어야 라이브로 반영됨


# 사용자가 우리에게 제출했을 때 / 우리가 계산하고 / 사용자에게 다시 보내주는 route