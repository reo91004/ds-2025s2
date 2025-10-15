"""
날짜: 2025-10-15
이름: 박용성
프로그램명: 우선순위 큐
프로그램 설명: 우선순위 큐 클래스 구현 및 테스트
"""

from PriorityQueue import PriorityQueue

q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)

print("PQueue: ", q)
while not q.isEmpty():
    print("Max Priority = ", q.dequeue())
