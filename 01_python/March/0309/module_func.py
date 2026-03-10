# datetime.date() : 연, 월, 일로 날짜를 표현할 때 사용하는 함수
import datetime

day = datetime.date(2021, 12, 14)
print(day)
print(day.weekday())    # 월 : 0, 화 : 1, 수 : 2, ... , 일 : 6
print()

# time.time() : UTC(Universal Time Coordinate, 협정 세계 표준시)를 사용하여
#               현재 시간을 실수 형태로 반환하는 함수
#               1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환
import time

print(time.time())
print()

# time.localtime : time.time()이 반환한 실숫값을 연, 월, 일, 시, 분, 초 ..... 형태로 바꿔주는 함수
print(time.localtime(time.time()))
print()

# time.strftime() : 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드 제공
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print()

# datetime 클래스 : 날짜와 시간을 동시에 표현하기 위해서 사용되며,
#                  위에서 다룬 date와 time 클래스에서 지원하는 대부분의 기능을 지원
from datetime import datetime

now = datetime.now()
print('현재 날씨와 시간:', now)
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print('포맷된 날짜와 시간:', formatted_date)
print('%s년 %s월 %s일 %s시 %s분 %s초' % (now.year, now.month, now.day, now.hour, now.minute, now.second))
print(datetime(2026, 3, 8, 10, 10, 10))
print(datetime(2026, 3, 8))
print()

# random 모듈 : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
# random() 함수 : 0부터 1사이의 랜덤 실수 반환
# uniform() 함수 : 2개의 숫자 사이의 랜덤 실수 반환
# randint() 함수 : 2개의 숫자 사이의 랜덤 정수 반환
#                 (2번째 인자로 넘어온 정수도 범위에 포함)
# choice() 함수 : 랜덤하게 하나의 원소를 선택
# sample() 함수 : 랜덤하게 여러 개의 원소를 선택
# shuffle() 함수 : 원소의 순서를 랜덤하게 변경
import random

print(random.random())                               # 0과 1 사이 난수 생성
print(random.uniform(1, 10))                    # 1과 10 사이 난수 생성
print(random.randint(1, 10))                    # 1부터 10 사이 정수형 난수 반환
print(random.randrange(0,100,2))       # 0부터 100사이 짝수(2 증가) 중 하나 선택
print(random.choice('abcdefghij'))
print(random.sample([1,2,3,4,5], 3))
items = [1,2,3,4,5,6,7]
random.shuffle(items)
print(items)
print()

# os 모듈 : 운영체제에서 제공하는 정보를 제공하거나 운영체제의 기능을 사용할 수 있는 방법을 제공
import os

print(os.name)                                    # 운영 체제의 종류를 반환
print(os.getcwd())                                # 현재 파일의 경로를 반환
print(os.path.join(os.getcwd(),'test'))           # 현재 경로와 문자를 연결시켜 반환
# os.mkdir(os.path.join(os.getcwd(),'test'))      # 가지고있는 정보를 가지고 디렉토리 제작
# os.rmdir(os.path.join(os.getcwd(),'test'))      # 해당 폴더가 비어있는 상태일 때만 삭제
# os.remove(os.path.join(os.getcwd(),'test.py'))  # 해당 파일을 삭제
os.chdir('C:\\Project\\Python_Source\\python311_01\\python\\March\\0309')  # 경로를 변경
print(os.getcwd())
print(os.listdir())                              # 현재 경로의 파일(디렉터리) 목록 확인하기


