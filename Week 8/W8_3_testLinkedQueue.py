"""
날짜: 2025-10-22
이름: 박용성
프로그램명: LinkedQueue test
프로그램 설명: 연결리스트로 큐 테스트 구현하기
"""

from LinkedQueue import LinkedQueue

q = LinkedQueue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.enqueue("F")
print("A B C D E F 삽입: ", q)

print("삭제 -->", q.dequeue())
print("삭제 -->", q.dequeue())
print("삭제 -->", q.dequeue())
print("3번의 삭제: ", q)

q.enqueue("G")
q.enqueue("H")
q.enqueue("I")
print("G H I 삽입: ", q)
