from sungjuk_class import Sungjuk


lst = []

def menu_title():
    print('\n*** 성적관리 ***')
    print('1. 성적정보 입력')
    print('2. 성적정보 출력')
    print('3. 성적정보 조회')
    print('4. 성적정보 수정')
    print('5. 성적정보 삭제')
    print('6. 프로그램 종료')


def input_sungjuk():
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    lst.append(obj)
    print('\n★ 성적정보 입력이 완료되었습니다 ★')


def print_sungjuk():
    if len(lst) == 0:
        print('\n※ 출력할 성적정보가 없습니다 ※')
        return
    print('\n%23s %s %s' % ('***', '성적표', '***'))
    print('=======================================================')
    print('학번    이름    국어    영어    수학    총점    평균    등급')
    print('=======================================================')
    tot_avg = 0
    for obj in lst:
        obj.output_sungjuk()
        # obj.avg => obj.get_avg()는 똑같은 역할을 수행
        tot_avg += obj.avg
    print('=======================================================')
    print('\t\t\t학생수 : %d\t\t\t전체 평균 : %5.2f' % (len(lst), tot_avg / len(lst)))
    print('=======================================================')


def search_sungjuk():
    code = input('\n성적을 조회할 학생의 학번을 입력하세요 => ')

    for data in lst:
        if code == data.code:
            print('\n학번    이름    국어    영어    수학    총점    평균    등급')
            print('=======================================================')
            data.output_sungjuk()
            print('=======================================================')
            break

    else:
        print('\n※ 해당 학번의 학생이 존재하지 않습니다 ※')


def update_sungjuk():
    code = input('\n성적을 수정할 학생의 학번을 입력하세요 => ')

    for data in lst:
        if code == data.code:
            data.kor = int(input('\n국어 점수를 새로 입력하세요 => '))
            data.eng = int(input('영어 점수를 새로 입력하세요 => '))
            data.math = int(input('수학 점수를 새로 입력하세요 => '))
            data.process_sungjuk()
            print('\n★ 해당 학생의 성적정보 수정이 완료되었습니다 ★')
            break

    else:
        print('\n※ 해당 학번의 성적정보가 존재하지 않습니다 ※')


def delete_sungjuk():
    code = input('\n성적을 삭제할 학생의 학번을 입력하세요 => ')

    for data in lst:
        if code == data.code:
            lst.remove(data)
            print('\n학번 %s 학생의 데이터 삭제' % code)
            print('\n★ 해당 학생의 성적정보가 삭제되었습니다 ★')
            break

    else:
        print('\n※ 해당 학번의 성적정보가 존재하지 않습니다 ※')


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



