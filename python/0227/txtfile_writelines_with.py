lines = ['안녕하세요\n', '파이썬\n', '도장입니다.\n']

with open('hello.txt', 'w', encoding='utf8') as file:
    file.writelines(lines)