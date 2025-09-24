import sys

a = []
for i in range(20):
    a.append(i)
    print(i, sys.getsizeof(a))  # 리스트의 메모리 크기 확인
