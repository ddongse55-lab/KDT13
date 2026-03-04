# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 'sangpum_data.txt'에 csv 형식으로 저장

# 'sangpum_data.txt'파일을 'write'모드로 열기
fp = open('sangpum_data.txt', 'w', encoding='utf-8')

# 제품코드, 제품명, 수량, 단가 입력
while True:
    dct = {}

    dct['code'] = input('제품코드 입력 => ')
    if dct['code'].lower() == 'exit':
        break
    dct['name'] = input('제품명 입력 => ')
    dct['su'] = int(input('수량 입력 => '))
    dct['price'] = int(input('단가 입력 => '))
    print()

    # 'sangpum_data.txt' 파일에 csv 형식으로 데이터 저장
    fp.write(dct['code'] + ',' + dct['name'] + ',' + str(dct['su']) + ',' + str(dct['price']) + '\n')

# 파일 닫기
fp.close()
