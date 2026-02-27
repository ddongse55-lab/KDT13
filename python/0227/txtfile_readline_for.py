with open('hello.txt', 'r', encoding='utf8') as file:
    for line in file:
        print(line.strip('\n')) # 줄바꿈이 한 번만 일어날 수 있도록
                                # print(line, end = '')과 동일한 역할을 함