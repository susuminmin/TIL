# 열기모드
# r: 일기, w: 쓰기(write - 오버라이트), a: 추가(append)
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'this is line {i + 1} \n')
f.close() # 해당 파일 종료

with open('with_ssafy.txt', 'w') as f: # context manager 블럭 생성함: # 연 파일 이름을 f로 지정하겠다. 
     for i in range(10):
         f.write(f"this is line {i + 1}\n") # 블럭 벗어나면 자동으로 클로즈

with open('ssafy.txt', 'w', encoding='utf-8') as f: #오픈한 파일 이름을 f로 삼겠다.
    f.writelines(['0\n', '1\n', '2\n', '3\n']) # 리스트로 받아서 여러 줄 쓸 수 있음
