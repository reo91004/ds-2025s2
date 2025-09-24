items = []


def insert(pos, elem):
    items.insert(pos, elem)


def delete(pos):
    return items.pop(pos)


def getEntry(pos):
    return items[pos]


def isEmpty():
    return len(items) == 0


def size():
    return len(items)


def clear():
    global items
    items = []


def find(item):
    return items.index(item)


def replace(pos, elem):
    items[pos] = elem


def sort():
    items.sort()


def merge(lst):
    items.extend(lst)


def display(msg="ArrayList: "):
    print(msg, size(), items)


print("최초 ", items)
insert(0, 10)
insert(0, 20)
insert(1, 30)
insert(3, 40)
insert(2, 50)
print("삽입x5 ", items)
delete(2)
print("삭제(2) ", items)
delete(3)
print("삭제(3) ", items)
delete(0)
print("삭제(0) ", items)

# 테스트 버전
items = []  # 리스트 초기화

display("파이썬 리스트로 구현한 리스트 테스트")
insert(0, 10)
insert(0, 20)
insert(1, 30)
insert(size(), 40)
insert(2, 50)
# 한 줄에 여러 문장
display("파이썬 리스트로 구현한 List(삽입x5) ")
sort()
display("파이썬 리스트로 구현한 List(정렬후) ")
replace(2, 90)
display("파이썬 리스트로 구현한 List(교체x1) ")
delete(2)
delete(size() - 1)
delete(0)
display("파이썬 리스트로 구현한 List(삭제x3) ")
lst = [1, 2, 3]
merge(lst)
display("파이썬 리스트로 구현한 List(병합) ")
clear()
display("파이썬 리스트로 구현한 List(정리후) ")
