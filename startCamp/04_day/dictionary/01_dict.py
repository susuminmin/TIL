# 딕셔너리 만들기
lunch1 = {
    '중국집': '02',
    '일식집': '032'
}
print(lunch1)

lunch2 = dict(중국집='02')
print(lunch2)

# 딕셔너리 내용 추가하기 (중국집은 이미 있으니까 key 값 넣으면 02 나왔겠지만... 분식집은 없으니까)
lunch1['분식집'] = '031'

# 딕셔너리 내용 가져오기 
idol = {
    'bts': {
        '지민': 24,
        'RM': 25
    }
}

# 랩몬스터의 나이는?
print(idol['bts']['RM'])

print("=====================================")

# 딕셔너리 반복문 활용하기
for key in lunch1:
    print(key, lunch1[key])


# value 만 가져오기
for value in lunch1.values():
    print(value)


# key 만 가져오기
for key in lunch1.keys():
    print(key)


# .items() => key, value 가져오기
for key, value in lunch1.items(): # tuple처럼 생김 / 첫번째를 key 두번째를 value로 접근해라~
    print(lunch1.items())
    print(key, value)