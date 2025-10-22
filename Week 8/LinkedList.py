"""
날짜: 2025-10-22
이름: 박용성
프로그램명: LinkedList
프로그램 설명: 연결리스트로 리스트 구현하기
"""


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.link
        return " -> ".join(map(str, elements))

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.link
        return count

    def getNode(self, pos):
        if pos < 0:
            return None
        current = self.head
        while pos > 0 and current:
            current = current.link
            pos -= 1
        return current

    def getEntry(self, pos):
        n = self.getNode(pos)
        if n:
            return n.data
        return None

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if self.head != None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
