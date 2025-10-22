"""
날짜: 2025-10-22
이름: 박용성
프로그램명: LinkedQueue
프로그램 설명: 연결리스트로 큐 구현하기
"""


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedQueue:
    def __init__(self):
        self.tail = None

    def __str__(self):
        arr = []
        if not self.isEmpty():
            node = self.tail.link
            while node != self.tail:
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
        return str(arr)

    def isEmpty(self):
        return self.tail is None

    def isFull(self):
        return False

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.tail = node
            node.link = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail == self.tail.link:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while node != self.tail:
                node = node.link
                count += 1
            return count
