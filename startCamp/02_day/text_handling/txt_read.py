f = open('ssafy.txt', 'r') # 어떤 모드로 파일을 여는지 정해줌
all_text = f.read() # all text 전체를 불러온다 (개행문자 포함!)
print(all_text)
f.close() # f로 열었을 때는 항상 close해주어야 함

with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)


with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip()) # 개행이나 공백을 지워줌