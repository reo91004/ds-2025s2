"""
날짜: 2025-10-15
이름: 박용성
프로그램명: 큐 실습
프로그램 설명: 원형 큐 상속 후 실습
"""

from CircularQueue import CircularQueue

# capacity가 8인 원형 큐 객체 생성
# 실제 최대 용량은 8-1이 됨
q = CircularQueue(8)

# A부터 F까지 7개의 요소를 삽입
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.enqueue("F")

# A B C D E F 삽입 후 큐 상태 출력
print("A B C D E F 삽입: ", q)

# 삭제 연산 3회 수행
print("삭제 -->", q.dequeue())
print("삭제 -->", q.dequeue())
print("삭제 -->", q.dequeue())

# 3번의 삭제 후 큐 상태 출력
print("      3번의 삭제: ", q)

# G H I 삽입
q.enqueue("G")
q.enqueue("H")
q.enqueue("I")

# G H I 삽입 후 큐 상태 출력
print("      G H I 삽입: ", q)
