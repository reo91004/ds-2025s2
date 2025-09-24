class Set:
    def __init__(self):
        # 원소 저장 리스트
        self.items = []

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        # 원소 e가 집합에 있는지 검사
        return item in self.items

    def insert(self, elem):
        # 중복 없는 삽입
        if elem not in self.items:
            self.items.append(elem)

    def delete(self, elem):
        # 원소가 있으면 삭제
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)  # 현재 집합 복사
        for elem in setB.items:
            if elem not in setC.items:
                setC.items.append(elem)
        return setC

    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC


setA = Set()
setA.insert("휴대폰")
setA.insert("지갑")
setA.insert("손수건")
setA.display("Set A:")

setB = Set()
setB.insert("빗")
setB.insert("파이썬 자료구조")
setB.insert("야구공")
setB.insert("지갑")
setB.display("Set B:")

setB.insert("빗")
setA.delete("손수건")
setA.delete("발수건")
setA.display("Set A:")
setB.display("Set B:")

# 합집합, 교집합, 차집합
setA.union(setB).display("A U B:")
setA.intersect(setB).display("A ^ B:")
setA.difference(setB).display("A - B:")
