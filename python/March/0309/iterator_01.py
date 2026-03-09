# __iter__ 메서드 -> 반복자 개체로 만들어주는 역할
it = [1, 2, 3].__iter__()
# __next__ 메서드 -> 반복자 개체에서 요소들에 접근하는 방법
#                   요소에 순차적으로 접근
print(it.__next__())
print(it.__next__())
print(it.__next__())
# StopIteration -> 반복 중단
#                  반복자 개체에서 모든 요소를 소모한 상태에서 다시 접근할 경우 발생
print(it.__next__())
