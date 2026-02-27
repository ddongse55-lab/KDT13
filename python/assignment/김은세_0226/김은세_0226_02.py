lst2 = []

while True:
    lst1 = []

    lst1.append(input('학번을 입력하세요: '))
    if lst1[0].lower() == 'exit':
        break
    lst1.append(input('이름을 입력하세요: '))
    lst1.append(int(input('국어 점수를 입력하세요: ')))
    lst1.append(int(input('영어 점수를 입력하세요: ')))
    lst1.append(int(input('수학 점수를 입력하세요: ')))
    lst1.append(lst1[2]+lst1[3]+lst1[4])
    lst1.append(lst1[5]/3)

    lst2.append(lst1)
    print()


print('\n%20s %s %-20s' %('***', '성적표', '***'))
print('=================================================')
print('학번    이름    국어    영어    수학    총점    평균')
print('=================================================')
total = 0
total_avg = 0

for lst1 in lst2:
    total += 1
    total_avg += lst1[-1]
    print('%s  %s  %4d   %4d   %4d    %4d    %4.2f' %
          (lst1[0], lst1[1], lst1[2], lst1[3], lst1[4], lst1[5], lst1[6]))
print('=================================================')
print('\t\t\t학생수 : %d\t\t\t전체 평균 : %5.2f' % (total, total_avg/total))
print('=================================================')