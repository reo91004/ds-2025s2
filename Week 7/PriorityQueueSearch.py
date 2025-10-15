"""
날짜: 2025-10-15
이름: 박용성
프로그램명: PriorityQueueSearch
프로그램 설명: 우선순위 큐에서, 미로 탐색을 위한 클래스 구현
"""

from PriorityQueue import PriorityQueue


class PriorityQueueSearch(PriorityQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    # 삽입 (우선순위에 따라 정렬하여 삽입)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size):
                if self.array[i][2] > self.array[highest][2]:  # 우선순위 비교
                    highest = i
            return highest
