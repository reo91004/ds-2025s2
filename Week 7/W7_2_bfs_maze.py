"""
날짜: 2025-10-15
이름: 박용성
프로그램명: BFS 미로
프로그램 설명: 원형 큐 이용한 BFS 미로 탐색
"""

from CircularQueue import CircularQueue

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


# BFS 미로 탐색
def BFS():
    que = CircularQueue(100)
    que.enqueue((0, 1))  # 시작 위치 (0, 1)
    print(f"({0}, {1})-> 현재 큐 : [{(0, 1)}]")

    while not que.isEmpty():
        here = que.dequeue()
        x, y = here[0], here[1]

        # 출구 'x'에 도달했는지 확인
        if map[y][x] == "x":
            return True
        else:
            map[y][x] = "."  # 방문한 위치 표시

            # 상하좌우 4방향 탐색
            directions = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            valid_positions = []

            for next_x, next_y in directions:
                if isValidPos(next_x, next_y):
                    que.enqueue((next_x, next_y))
                    valid_positions.append((next_x, next_y))

            print(f"({x}, {y})-> 현재 큐 : {valid_positions}")

    return False


# 프로그램 실행
result = BFS()
if result:
    print(" --> 미로탐색 성공")
else:
    print(" --> 미로탐색 실패")
