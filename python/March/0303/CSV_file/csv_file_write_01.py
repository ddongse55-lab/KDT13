import csv

# 파일 열기
f = open('output.csv', 'w', encoding ='utf-8', newline ='')

# delimiter = ',' : 구분자 지정 (default는 ','로 설정되어 있음)
# quotechar = '"' : 데이터를 묶을 문자 지정
# csv.QUOTE_ALL : 모두 사용하겠다는 의미
wr = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)

# writerow() : 행단위로 출력
wr.writerow((1, '김정수', False))
wr.writerow([2, '박상미', True])

# 파일 닫기
f.close()