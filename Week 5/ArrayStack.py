"""
날짜: 2025-10-01
이름: 박용성
프로그램명: 파이썬 ArrayStack 구현
프로그램 설명: 클래스를 이용한 리스트 기반 스택 구현
"""


class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def __str__(self):
        return str(self.array[0 : self.top + 1])

    # 스택의 연산들을 멤버 함수로 구현
    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
