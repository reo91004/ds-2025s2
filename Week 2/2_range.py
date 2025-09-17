# 25.09.17 실습
# 2020039069 박용성

for n in range(5):
    pass

for n in range(2, 10):
    pass

for n in range(10, 3, -2):
    pass

for item in [12, 33, 52, 26, 99]:
    print("값= ", item)

for c in "Game Over !":
    print("값= ", c)

mySet = set([12, 33, 52, 26, 99])
for e in mySet:
    print("값= ", e)

myDict = {"A": 12, "B": 33, "C": 52, "D": 26, "E": 99}
for e in myDict:
    print("키= ", e)
    print("값= ", myDict[e])
