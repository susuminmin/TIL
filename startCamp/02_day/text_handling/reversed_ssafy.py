with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # 각 라인을 item 으로, list 의 형태로 반환
    # print(lines)

# with open('reversed_ssafy.txt', 'w', encoding='utf-8') as f: #오픈한 파일 이름을 f로 삼겠다.
#     numbers = (['0\n', '1\n', '2\n', '3\n'])
#     f.writelines(reversed(numbers))

lines.reverse() # list를 반대로 뒤집는다. 반환은 안 하고 뒤집기만 하는듯?!
print(lines) 

with open('reversed_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)