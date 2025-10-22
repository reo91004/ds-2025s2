"""
날짜: 2025-10-22
이름: 박용성
프로그램명: DoublyLinkedDeque test
프로그램 설명: 이중 연결 리스트로 덱 테스트 구현하기
"""

from DoublyLinkedDeque import DoublyLinkedDeque

dq = DoublyLinkedDeque()

# 홀수는 addFront(), 짝수는 addRear() 수행
for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
print("홀수->전단, 짝수->후단: ", dq)

# 전단 2회 삭제, 후단 3회 삭제
for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
print(" 전단삭제x2 후단삭제x3: ", dq)

# 9~13을 전단에 삽입
for i in range(9, 14):
    dq.addFront(i)
print("   전단삽입 9,10,...13: ", dq)
