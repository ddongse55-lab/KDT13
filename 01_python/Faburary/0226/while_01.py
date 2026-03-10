even = 0                   # 초기식
odd = 0
count = 0

while count < 100:         # 조건식
    count += 1             # 증감식
    if count % 2 == 0:     # 반복 처리할 내용
        even += count
    else:
        odd += count

print('홀수의 합 :', odd)
print('짝수의 합 :', even)