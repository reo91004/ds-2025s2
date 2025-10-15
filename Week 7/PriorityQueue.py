"""
날짜: 2025-10-15
이름: 박용성
프로그램명: PriorityQueue
프로그램 설명: 우선순위 큐 클래스 구현
"""


class PriorityQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity  # 큐의 용량
        self.array = [None] * capacity  # 내부 배열
        self.size = 0  # 현재 요소 수

    def __str__(self):
        return str(self.array[: self.size])

    # 비어 있는지 확인
    def isEmpty(self):
        return self.size == 0

    # 가득 찼는지 확인
    def isFull(self):
        return self.size == self.capacity

    # 삽입 (맨 뒤에 추가)
    def enqueue(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1
        else:
            print("PriorityQueue is full")

    # 최고 우선순위 인덱스 찾기
    def findMaxIndex(self):
        if self.isEmpty():
            return -1
        highest = 0
        for i in range(1, self.size):
            if self.array[i] > self.array[highest]:
                highest = i
        return highest

    # 삭제 (최고 우선순위 요소)
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest != -1:
            # 맨 뒤 요소와 교체 후 삭제
            self.size -= 1
            self.array[highest], self.array[self.size] = (
                self.array[self.size],
                self.array[highest],
            )
            return self.array[self.size]
        else:
            print("PriorityQueue is empty")

    # 최고 우선순위 요소 탐색 (삭제 없이 반환)
    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.array[highest]
        else:
            print("PriorityQueue is empty")
