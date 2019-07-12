"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# total_score = score['수학'] + score['국어'] + score['음악']
# avg = 1/3 * total
# print(avg)

# sum(score.values()) 로 total_score 계산해도 됨

total_score = 0

for subject_score in score.values():
    total_score = total_score + subject_score

avg_score = total_score / len(score.values())
print(avg_score)



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
total = 0
count = 0

# avg_a = ( scores['a']['수학'] + scores['a']['국어'] + scores['a']['음악'] ) * 1/3
# avg_b = ( scores['b']['수학'] + scores['b']['국어'] + scores['b']['음악'] ) * 1/3
# total_avg = (avg_a + avg_b) / 2
# print(total_avg)

for person_score in scores.values():
    total += sum(person_score.values())
    count += len(person_score)

avg = total / count 
print(avg)



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

# for key in city:
#     print(key, ":", (city[key][0] + city[key][1] + city[key][2]) / 3 )

for key, value in city.items():
    average_temp = sum(value) / len(value)
    # print(key, average_temp)
    print(f'{key} : {average_temp}')



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')







# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in city['서울']:
    print("Yes")
else:
    print("No")