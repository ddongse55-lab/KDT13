# 운영체제와 관련된 모듈
import os

# 운영체제 경로 내에 'sangpum_data.txt' 파일의 존재 유무 확인
if os.path.exists('sangpum_data.txt'):
    # 'sangpum_data.txt' 파일 'read' 모드로 열기
    fp = open('sangpum_data.txt', 'r', encoding='utf-8')
    lst = []

    # 'sangpum_data.txt' 파일 내의 데이터를 딕셔너리에 저장
    for line in fp:
        res = line.strip('\n').split(',')
        dct = {}
        dct['code'] = res[0]
        dct['name'] = res[1]
        dct['su'] = int(res[2])
        dct['price'] = int(res[3])
        dct['charge'] = dct['su'] * dct['price']

        lst.append(dct)

    # 파일 닫기
    fp.close()

    # 'sangpum_data.txt' 파일 내의 데이터 출력
    print('\n\t\t\t\t*** 제품관리 ***')
    print('============================================')
    print('제품코드    제품명     수량      단가    판매금액')
    print('============================================')
    total = 0
    for dct in lst:
        total += dct['charge']
        print('%5s    %5s   %4d   %7d   %7d'
              % (dct['code'], dct['name'], dct['su'], dct['price'], dct['charge']))
    print('============================================')
    print('\t\t\t\t 총 금액은', total, '원 입니다.')
    print('============================================')

# 운영체제 내에 파일이 존재하지 않는 경우
else:
    print('파일이 존재하지 않습니다!!!')