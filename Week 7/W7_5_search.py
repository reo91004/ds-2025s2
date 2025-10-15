"""
날짜: 2025-10-15
이름: 박용성
프로그램명: PriorityQueueSearch를 이용한 미로 탐색
프로그램 설명: 우선순위 큐에서, 미로 탐색을 위한 클래스 구현 후 실습
"""

from PriorityQueueSearch import PriorityQueueSearch
import math

(ox, oy) = (5, 4)  # 출구 위치


def dist(x, y):
    return math.sqrt((x - ox) ** 2 + (y - oy) ** 2)


# 미로 맵 정의
map = [
    ["1", "1", "1", "1", "1", "1"],
    ["e", "0", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "1", "1"],
    ["1", "0", "1", "0", "1", "1"],
    ["1", "0", "1", "0", "0", "x"],
    ["1", "1", "1", "1", "1", "1"],
]

MAZE_SIZE = 6


# 유효한 위치인지 확인하는 함수
def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == "0" or map[y][x] == "x"


def MySmartSearch():
    q = PriorityQueueSearch()
    q.enqueue((0, 1, -dist(0, 1)))  # (현재 위치, 이전 위치, 우선순위)
    print(
        "PQueue: ",
    )

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end="->")
        x, y, _ = here
        if map[y][x] == "x":
            return True
        else:
            map[y][x] = "."
            if isValidPos(x, y - 1):
                q.enqueue((x, y - 1, -dist(x, y - 1)))
            if isValidPos(x, y + 1):
                q.enqueue((x, y + 1, -dist(x, y + 1)))
            if isValidPos(x - 1, y):
                q.enqueue((x - 1, y, -dist(x - 1, y)))
            if isValidPos(x + 1, y):
                q.enqueue((x + 1, y, -dist(x + 1, y)))
            print(" 우선순위 큐 : ", q)
    return False


result = MySmartSearch()
if result:
    print(" --> 미로탐색 성공")
else:
    print(" --> 미로탐색 실패")
