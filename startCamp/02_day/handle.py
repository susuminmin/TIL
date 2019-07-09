import os

# 500개의 지원서가 있는 곳으로 이동 
os.chdir(r'C:\Users\student\TIL\startCamp\02_day')

filenames = os.listdir('.')
for filename in filenames:
    
    # 확장자가 .txt 인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리
    
    if extension == '.txt':
        print('이름을 바꾼다.', filename)
        # os.rename(filename, f'SAMSUNG_{filename}') # 첫번째 인자로 넘어간 이름을, 두번째 인자로 넘어간 이름으로 바꾼다.
        os.rename(filename, filename.replace("SAMSUNG_", "SSAFY_")) # 여기서 filename은 str 타입임
    
