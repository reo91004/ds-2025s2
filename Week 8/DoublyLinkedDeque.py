"""
날짜: 2025-10-22
이름: 박용성
프로그램명: DoublyLinkedDeque test
프로그램 설명: 이중 연결 리스트로 덱(Deque) 구현 및 테스트
"""


# ------------------------------------------
# 이중 연결 리스트를 위한 노드 클래스
# ------------------------------------------
class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem  # 노드의 데이터
        self.prev = prev  # 이전 노드 포인터
        self.next = next  # 다음 노드 포인터


# ------------------------------------------
# 연결된 덱 클래스 (Doubly Linked Deque)
# ------------------------------------------
class DoublyLinkedDeque:
    def __init__(self):
        self.front = None  # 덱의 앞쪽 포인터
        self.rear = None  # 덱의 뒤쪽 포인터

    # 공백 상태 확인
    def isEmpty(self):
        return self.front is None

    # 덱 초기화
    def clear(self):
        self.front = self.rear = None

    # 앞쪽에 원소 삽입
    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            # 공백 상태면 front, rear 모두 node로 설정
            self.front = self.rear = node
        else:
            # 기존 front의 prev를 새 노드로 연결
            self.front.prev = node
            # front 갱신
            self.front = node

    # 뒤쪽에 원소 삽입
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            # 공백 상태면 front, rear 모두 node로 설정
            self.front = self.rear = node
        else:
            # 기존 rear의 next를 새 노드로 연결
            self.rear.next = node
            # rear 갱신
            self.rear = node

    # 앞쪽 원소 삭제
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front is None:  # 노드가 하나뿐이었을 경우
                self.rear = None
            else:
                self.front.prev = None
            return data

    # 뒤쪽 원소 삭제
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear is None:  # 노드가 하나뿐이었을 경우
                self.front = None
            else:
                self.rear.next = None
            return data

    # 문자열 변환 (출력용)
    def __str__(self):
        arr = []
        node = self.front
        while node is not None:
            arr.append(node.data)
            node = node.next
        return str(arr)
