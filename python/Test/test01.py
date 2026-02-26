score = map(int, input().split())

if score < 0 or score > 100:
    print('잘못된 점수')

avg = sum(score)/4

if avg >= 80:
    print('합격')
else:
    print('불합격')