import random

# ver_1
a = list(range(1, 46))
print('★로또 번호를 추첨합니다★')
print(random.sample(a, 6))

print()

# ver_2
lst = []
count = 0
while True:
    num = random.randint(1, 45)

    if len(lst) == 0:
        lst.append(num)

    for i in lst:
        if i == num:
            break
    else:
        lst.append(num)
        count += 1

    if count == 5:
        break

print('★로또 번호를 추첨합니다★')
print(lst)




