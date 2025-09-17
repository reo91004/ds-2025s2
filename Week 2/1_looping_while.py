# 25.09.17 실습
# 2020039069 박용성

dan = int(input("구구단 입력: "))

n = 2
while n < 10:
    print("%2d x %2d = " % (dan, n), dan * n)
    n += 1
