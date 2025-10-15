"""
날짜: 2025-10-15
이름: 박용성
프로그램명: CircularDeque
프로그램 설명: 원형 덱 클래스 구현
"""

from CircularQueue import CircularQueue


class CircularDeque(CircularQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            # 전단 삽입: 비워둔 슬롯(front)에 기록 후 front를 한 칸 뒤로 이동
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print("Deque is full")  # 덱이 가득 찼을 때의 처리

    def deleteRear(self):
        if not self.isEmpty():
            # 후단 삭제: 현재 rear의 항목을 반환하고 rear를 한 칸 뒤로 이동
            item = self.array[self.rear]
            self.array[self.rear] = None  # 선택 사항: 제거된 위치를 None으로 설정
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else:
            print("Deque is empty")  # 덱이 비어 있을 때의 처리

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            print("Deque is empty")  # 덱이 비어 있을 때의 처리
