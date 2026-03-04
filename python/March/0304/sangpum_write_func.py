# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 'sangpum_data.csv'에 csv 형식으로 저장
import csv
import os

def menu_title():
    print('\n*** 제품정보 관리 ***')
    print('1. 제품정보 입력')
    print('2. 제품정보 출력')
    print('3. 제품정보 조회')
    print('4. 제품정보 수정')
    print('5. 제품정보 삭제')
    print('6. 프로그램 종료')


def input_data():
    # 데이터를 입력받아 파일로 저장
    if os.path.exists('sangpum_data.csv'):
        # 'sangpum_data.csv'파일을 'add'모드로 열기
        fp = open('sangpum_data.csv', 'a', encoding='utf-8', newline='')
        fieldnames = ['code', 'name', 'su', 'price', 'charge']
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        # 'sangpum_data.csv'파일을 'add'모드로 열기
        fp = open('sangpum_data.csv', 'a', encoding='utf-8', newline='')
        fieldnames = ['code', 'name', 'su', 'price', 'charge']
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    dct = {}
    dct['code'] = input('\n제품코드 입력 => ')
    dct['name'] = input('제품명 입력 => ')
    dct['su'] = int(input('수량 입력 => '))
    dct['price'] = int(input('단가 입력 => '))
    print()

    dct['charge'] = dct['su'] * dct['price']

    wr.writerow(dct)
    fp.close()

    print('★ 제품정보 입력이 완료되었습니다 ★')


def print_data():
    # 파일에 저장되어 있는 데이터를 모두 출력
    if os.path.exists('sangpum_data.csv'):
        # 'sangpum_data.txt' 파일 'read' 모드로 열기
        fp = open('sangpum_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        print('\n\t\t\t\t*** 제품관리 ***')
        print('============================================')
        print('제품코드    제품명     수량      단가    판매금액')
        print('============================================')
        total = 0
        for data in lst:
            total += int(data['charge'])
            print('%5s    %5s   %4d   %7d   %7d'
                  % (data['code'], data['name'], int(data['su']), int(data['price']), int(data['charge'])))
        print('============================================')
        print('\t\t\t\t 총 금액은', total, '원 입니다.')
        print('============================================')

        fp.close()

    else:
        print('\n※ 출력할 제품 정보가 없습니다 ※')


def search_data():
    # 제품코드를 입력받아 해당 제품 정보를 출력
    if os.path.exists('sangpum_data.csv'):
        # 'sangpum_data.txt' 파일 'read' 모드로 열기
        fp = open('sangpum_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        code = input('\n조회할 제품의 코드를 입력하세요 => ')

        for data in lst:
            if code == data['code']:
                print('\n제품코드    제품명     수량      단가    판매금액')
                print('============================================')
                print('%5s    %5s   %4d   %7d   %7d'
                      % (data['code'], data['name'], int(data['su']), int(data['price']), int(data['charge'])))
                print('============================================')
                break

        else:
            print('\n※ 해당 코드의 제품이 존재하지 않습니다 ※')

        fp.close()

    else:
        print('\n※ 조회할 제품 정보가 없습니다 ※')


def update_data():
    # 제품코드를 입력받아 일치하는 데이터를 찾아서 수량과 단가를 입력받아 금액을 수정 후 파일 전체를 재저장
    if os.path.exists('sangpum_data.csv'):
        # 'sangpum_data.txt' 파일 'read' 모드로 열기
        fp = open('sangpum_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        code = input('\n수정할 제품의 코드를 입력하세요 => ')

        flag = 0
        for data in lst:
            if code == data['code']:
                data['su'] = int(input('수량을 입력하세요 => '))
                data['price'] = int(input('단가를 입력하세요 => '))
                data['charge'] = data['su'] * data['price']
                flag = 1
                break

        else:
            print('\n※ 해당 코드의 제품이 존재하지 않습니다 ※')

        fp.close()

        if flag == 1:
            fp2 = open('sangpum_data.csv', 'w', encoding='utf-8', newline='')
            fieldnames = ['code', 'name', 'su', 'price', 'charge']
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)

            fp2.close()

            print('\n★ 제품정보 수정이 완료되었습니다 ★')

    else:
        print('\n※ 수정할 제품 정보가 없습니다 ※')


def delete_data():
    # 제품코드를 입력받아 일치하는 데이터를 찾아서 해당 데이터를 삭제
    if os.path.exists('sangpum_data.csv'):
        # 'sangpum_data.txt' 파일 'read' 모드로 열기
        fp = open('sangpum_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        code = input('\n삭제할 제품의 코드를 입력하세요 => ')

        flag = 0
        for data in lst:
            if code == data['code']:
                flag = 1
                lst.remove(data)
                print('\n제품코드 %s 데이터 삭제' % code)
                break
        else:
            print('\n※ 해당 코드의 제품이 존재하지 않습니다 ※')

        fp.close()

        if flag == 1:
            fp2 = open('sangpum_data.csv', 'w', encoding='utf-8', newline='')
            fieldnames = ['code', 'name', 'su', 'price', 'charge']
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)

            fp2.close()

            print('\n★ 제품정보가 삭제되었습니다 ★')

    else:
        print('\n※ 수정할 제품 정보가 없습니다 ※')




if __name__ == '__main__':
    while True:
        menu_title()
        menu = input('\n메뉴를 선택하세요(1~6) => ')
        if menu == '1':
            input_data()
        elif menu == '2':
            print_data()
        elif menu == '3':
            search_data()
        elif menu == '4':
            update_data()
        elif menu == '5':
            delete_data()
        elif menu == '6':
            print('\n★ 프로그램을 종료합니다 ★')
            break
        else:
            print('\n※ 잘못된 접근입니다')
            print('메뉴를 다시 입력하세요 ※')

