"""
날짜: 2025-10-15
이름: 박용성
프로그램명: 덱 실습
프로그램 설명: 원형 덱 상속 후 실습
"""

from CircularDeque import CircularDeque


dq = CircularDeque(10)

for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
print("홀수->전단, 짝수->후단: ", dq)

for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
print(" 전단삭제x2 후단삭제x3: ", dq)

for i in range(9, 14):
    dq.addFront(i)
print("  전단삽입 9, 10, ... , 13: ", dq)
