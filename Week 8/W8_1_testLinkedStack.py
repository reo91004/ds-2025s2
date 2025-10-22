"""
날짜: 2025-10-22
이름: 박용성
프로그램명: LinkedStack 테스트
프로그램 설명: 연결리스트로 스택 구현 테스트
"""

from LinkedStack import LinkedStack

if __name__ == "__main__":
    s = LinkedStack()

    print("스택: ", s)
    msg = input("문자열 입력: ")
    for c in msg:
        s.push(c)

    print("스택 : ", s)
    print("문자열 출력: ", end="")

    while not s.is_empty():
        print(s.pop(), end="")
    print()  # 개행
    print("스택: ", s)
