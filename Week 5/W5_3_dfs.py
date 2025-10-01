"""
날짜: 2025-10-01
이름: 박용성
프로그램명: Infix2Postfix 구현
프로그램 설명: 중위 표현식을 후위 표현식으로 변환하는 프로그램 구현
"""

from ArrayStack import ArrayStack

# fmt: off
map = [
    ["1", "1", "1", "1", "1", "1"],
    ["e", "0", "0", "0", "0", "1"],
    ["1", "0", "1", "0", "1", "1"],
    ["1", "1", "1", "0", "0", "x"],
    ["1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1"],
]
# fmt: on


def isValidPos(x, y):
    # 미로의 세로, 가로 크기
    if x < 0 or y < 0 or y >= len(map) or x >= len(map[0]):
        return False

    # 벽('1')은 못 가고, 빈 칸('0') 또는 도착점('x')만 가능
    if map[y][x] == "0" or map[y][x] == "x":
        return True
    else:
        return False


def DFS():
    print("DFS: ")
    stack = ArrayStack(100)  # 최대 크기 100인 스택 생성
    stack.push((0, 1))  # 시작 위치 (0,1) push

    while not stack.isEmpty():  # 스택이 빌 때까지 반복
        here = stack.pop()  # 현재 위치 꺼내기
        print(here, end="->")  # 경로 출력
        (x, y) = here  # 좌표 분리

        if map[y][x] == "x":  # 목표 지점 도착 시
            return True

        else:
            map[y][x] = "."  # 현재 위치는 방문함 표시 (.)

            # 우
            if isValidPos(x + 1, y):
                stack.push((x + 1, y))
            # 좌
            if isValidPos(x - 1, y):
                stack.push((x - 1, y))
            # 하
            if isValidPos(x, y + 1):
                stack.push((x, y + 1))
            # 상
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))

            # 교재와 반대로 넣어야 함

            print(" 현재 스택: ", stack)

    return False  # 탐색 실패


result = DFS()
if result:
    print(" --> 탐색 성공")
else:
    print(" --> 탐색 실패")
