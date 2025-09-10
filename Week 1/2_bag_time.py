# 25.09.10
# 2020039069 박용성

# 가방(Bag) 구현 및 실행 시간 측정

import time


def contains(bag, e):
    return e in bag


def insert(bag, e):
    bag.append(e)


def remove(bag, e):
    bag.remove(e)


def count(bag):
    return len(bag)


myBag = []
start = time.time()

for _ in range(10000000):
    insert(myBag, "휴대폰")

end = time.time()

print("실행 시간: ", end - start)
