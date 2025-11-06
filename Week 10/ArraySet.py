"""
날짜: 2025-11-05
이름: 박용성
프로그램명: ArraySet
프로그램 설명: 정렬된 배열을 사용한 집합 구현
"""


# 정렬된 배열을 사용한 집합 구현
class SortedArraySet:
    def __init__(self):
        self.array = []
        self.size = 0

    def __str__(self):
        return str(self.array)

    def display(self, msg):
        print(msg, self.array)

    def contains(self, item):
        return item in self.array

    def insert(self, elem):
        # 정렬을 유지하면서 삽입
        if elem not in self.array:
            self.array.append(elem)
            self.array.sort()
            self.size += 1

    def delete(self, elem):
        if elem in self.array:
            self.array.remove(elem)
            self.size -= 1

    def __eq__(self, setB):
        if self.size != setB.size:
            return False

        for i in range(self.size):
            if self.array[i] != setB.array[i]:
                return False
        return True

    def union(self, setB):
        # 합집합: 정렬된 두 배열을 병합
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]
            if a == b:
                setC.append(a)
                i += 1
                j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1

        while j < setB.size:
            setC.append(setB.array[j])
            j += 1

        return setC

    def intersect(self, setB):
        # 교집합: 두 배열에서 공통 원소만 추출
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]
            if a == b:
                setC.append(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1

        return setC

    def difference(self, setB):
        # 차집합: self에만 있고 setB에는 없는 원소
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]
            if a == b:
                i += 1
                j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1

        return setC

    def append(self, elem):
        # 정렬 상태를 유지하면서 직접 추가 (내부 사용)
        self.array.append(elem)
        self.size += 1


# 테스트 코드
if __name__ == "__main__":
    import random

    setA = SortedArraySet()
    setB = SortedArraySet()
    for i in range(5):
        setA.insert(random.randint(1, 9))
        setB.insert(random.randint(1, 9))

    print("Set A:", setA)
    print("Set B:", setB)
    print("A U B:", setA.union(setB))
    print("A ^ B:", setA.intersect(setB))
    print("A - B:", setA.difference(setB))
