"""
날짜: 2025-10-22
이름: 박용성
프로그램명: LinkedStack
프로그램 설명: 연결리스트로 스택 구현하기
"""


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def __str__(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.link
        return " -> ".join(map(str, elements))

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.is_empty():
            n = self.top.data
            self.top = self.top.link
            return n

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.link
        return count
