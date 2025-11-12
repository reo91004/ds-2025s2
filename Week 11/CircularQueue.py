"""
날짜: 2025-10-15
이름: 박용성
프로그램명: CircularQueue
프로그램 설명: 원형 큐 클래스 구현
"""


class CircularQueue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = 0
        self.capacity = capacity  # 모듈러 밑은 배열 길이 N
        self.array = [None] * capacity  # 실제 저장소 크기 = N
        # 유효 저장 가능 개수 = N-1 (한 칸 비움)

    def __str__(self):
        if self.isEmpty():
            return "[]"
        if self.front < self.rear:
            return str(self.array[self.front + 1 : self.rear + 1])
        return str(
            self.array[self.front + 1 : self.capacity] + self.array[0 : self.rear + 1]
        )

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.array[(self.front + 1) % self.capacity]

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        self.front = (self.front + 1) % self.capacity
        item = self.array[self.front]
        self.array[self.front] = None  # 선택 사항: 시각적/디버깅용 클리어
        return item
