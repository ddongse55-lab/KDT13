import csv
import os

def menu_title():
    print('\n*** 성적관리 ***')
    print('1. 성적정보 입력')
    print('2. 성적정보 출력')
    print('3. 성적정보 조회')
    print('4. 성적정보 수정')
    print('5. 성적정보 삭제')
    print('6. 프로그램 종료')


def grade(avg):
    # 성적의 등급을 판별하는 함수
    if avg >= 90:
        grade = '수'
    elif avg >= 80:
        grade = '우'
    elif avg>= 70:
        grade = '미'
    elif avg >= 60:
        grade = '양'
    else:
        grade = '가'

    return grade


def input_sungjuk():
    # 데이터를 입력받아 파일로 저장
    if os.path.exists('sungjuk_data.csv'):
        # 'sungjuk_data.csv'파일을 'add'모드로 열기
        fp = open('sungjuk_data.csv', 'a', encoding='utf-8', newline='')
        fieldnames = ['code', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'grade']
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        # 'sungjuk_data.csv'파일을 'add'모드로 열기
        fp = open('sungjuk_data.csv', 'a', encoding='utf-8', newline='')
        fieldnames = ['code', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'grade']
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    dct = {}
    dct['code'] = input('\n학번을 입력하세요: ')
    dct['name'] = input('이름을 입력하세요: ')
    dct['kor'] = int(input('국어 점수를 입력하세요: '))
    dct['eng'] = int(input('영어 점수를 입력하세요: '))
    dct['math'] = int(input('수학 점수를 입력하세요: '))
    dct['total'] = dct['kor'] + dct['eng'] + dct['math']
    dct['avg'] = dct['total'] / 3
    dct['grade'] = grade(dct['avg'])

    wr.writerow(dct)
    fp.close()

    print('\n★ 성적정보 입력이 완료되었습니다 ★')


def print_sungjuk():
    # 파일에 저장되어 있는 데이터를 모두 출력
    if os.path.exists('sungjuk_data.csv'):
        # 'sungjuk_data.csv' 파일 'read' 모드로 열기
        fp = open('sungjuk_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        print('\n%23s %s %-23s' % ('***', '성적표', '***'))
        print('=======================================================')
        print('학번    이름    국어    영어    수학    총점    평균    등급')
        print('=======================================================')
        total = 0
        total_avg = 0
        for dct in lst:
            total += 1
            total_avg += float(dct['avg'])
            print('%s  %s  %4d   %4d   %4d    %4d    %4.2f    %s' %
                  (dct['code'], dct['name'], int(dct['kor']), int(dct['eng']), int(dct['math']),
                   int(dct['total']), float(dct['avg']), dct['grade']))
        print('=======================================================')
        print('\t\t\t학생수 : %d\t\t\t전체 평균 : %5.2f' % (total, total_avg / total))
        print('=======================================================')

        fp.close()

    else:
        print('\n※ 출력할 성적정보가 없습니다 ※')


def search_sungjuk():
    # 학번을 입력받아 해당 학생의 성적정보를 출력
    if os.path.exists('sungjuk_data.csv'):
        # 'sungjuk_data.csv' 파일 'read' 모드로 열기
        fp = open('sungjuk_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        code = input('\n성적을 조회할 학생의 학번을 입력하세요 => ')

        for dct in lst:
            if code == dct['code']:
                print('\n학번    이름    국어    영어    수학    총점    평균    등급')
                print('=======================================================')
                print('%s  %s  %4d   %4d   %4d    %4d    %4.2f    %s' %
                      (dct['code'], dct['name'], int(dct['kor']), int(dct['eng']), int(dct['math']),
                       int(dct['total']), float(dct['avg']), dct['grade']))
                print('=======================================================')
                break

        else:
            print('\n※ 해당 학번의 학생이 존재하지 않습니다 ※')

        fp.close()

    else:
        print('\n※ 조회할 성적 정보가 없습니다 ※')


def update_sungjuk():
    # 학번을 입력받아 일치하는 데이터를 찾아서 해당 학생의 국어/영어/수학 점수를 입력받아 총점/평균/등급을 수정 후 파일 전체를 재저장
    if os.path.exists('sungjuk_data.csv'):
        # 'sungjuk_data.csv' 파일 'read' 모드로 열기
        fp = open('sungjuk_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        code = input('\n성적을 수정할 학생의 학번을 입력하세요 => ')

        flag = 0
        for dct in lst:
            if code == dct['code']:
                dct['kor'] = int(input('\n국어 점수를 새로 입력하세요 => '))
                dct['eng'] = int(input('영어 점수를 새로 입력하세요 => '))
                dct['math'] = int(input('수학 점수를 새로 입력하세요 => '))
                dct['total'] = dct['kor'] + dct['eng'] + dct['math']
                dct['avg'] = dct['total'] / 3
                dct['grade'] = grade(dct['avg'])

                flag = 1
                break

        else:
            print('\n※ 해당 학번의 성적정보가 존재하지 않습니다 ※')

        fp.close()

        if flag == 1:
            fp2 = open('sungjuk_data.csv', 'w', encoding='utf-8', newline='')
            fieldnames = ['code', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'grade']
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)

            fp2.close()

            print('\n★ 해당 학생의 성적정보 수정이 완료되었습니다 ★')

    else:
        print('\n※ 수정할 성적 정보가 없습니다 ※')


def delete_sungjuk():
    # 학번을 입력받아 일ㅊ치하는 데이터를 찾아 해당 학생의 성적정보를 모두 삭제
    if os.path.exists('sungjuk_data.csv'):
        # 'sungjuk_data.csv' 파일 'read' 모드로 열기
        fp = open('sungjuk_data.csv', 'r', encoding='utf-8', newline='')
        lst = list(csv.DictReader(fp))

        code = input('\n성적을 삭제할 학생의 학번을 입력하세요 => ')

        flag = 0
        for dct in lst:
            if code == dct['code']:
                lst.remove(dct)
                print('\n학번 %s 학생의 데이터 삭제' % code)
                flag = 1
                break

        else:
            print('\n※ 해당 학번의 성적정보가 존재하지 않습니다 ※')

        fp.close()

        if flag == 1:
            fp2 = open('sungjuk_data.csv', 'w', encoding='utf-8', newline='')
            fieldnames = ['code', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'grade']
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)

            fp2.close()

            print('\n★ 해당 학생의 성적정보가 삭제되었습니다 ★')

    else:
        print('\n※ 삭제할 성적 정보가 없습니다 ※')


if __name__ == '__main__':
    while True:
        menu_title()
        menu = input('\n메뉴를 선택하세요(1~6) => ')
        if menu == '1':
            input_sungjuk()
        elif menu == '2':
            print_sungjuk()
        elif menu == '3':
            search_sungjuk()
        elif menu == '4':
            update_sungjuk()
        elif menu == '5':
            delete_sungjuk()
        elif menu == '6':
            print('\n★ 프로그램을 종료합니다 ★')
            break
        else:
            print('\n※ 잘못된 접근입니다')
            print('메뉴를 다시 입력하세요 ※')
