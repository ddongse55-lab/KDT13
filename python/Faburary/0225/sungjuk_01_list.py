sungjuk = []

sungjuk.append(input('학번을 입력하세요: '))
sungjuk.append(input('이름을 입력하세요: '))
sungjuk.append(int(input('국어 점수를 입력하세요: ')))
sungjuk.append(int(input('영어 점수를 입력하세요: ')))
sungjuk.append(int(input('수학 점수를 입력하세요: ')))
sungjuk.append(sungjuk[2]+sungjuk[3]+sungjuk[4])
sungjuk.append(sungjuk[5]/3)

print('%20s %s %-20s' %('***', '성적표', '***'))
print('=================================================')
print('학번    이름    국어    영어    수학    총점    평균')
print('=================================================')
print('%s  %s  %4d   %4d   %4d    %4d    %4.2f' %
      (sungjuk[0], sungjuk[1], sungjuk[2], sungjuk[3], sungjuk[4], sungjuk[5], sungjuk[6]))
print('=================================================')