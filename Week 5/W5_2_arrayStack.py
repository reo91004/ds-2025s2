"""
날짜: 2025-10-01
이름: 박용성
프로그램명: Stack Class 실습
프로그램 설명: Class로 구현한 Stack 사용 실습
"""

from ArrayStack import ArrayStack

s = ArrayStack(100)

msg = input("문자열 입력: ")
for c in msg:
    s.push(c)

print("문자열 출력: ", end="")
while not s.isEmpty():
    print(s.pop(), end="")
print()

# 방법 1
s = ArrayStack(10)
for i in range(1, 6):
    s.push(i)
print(" push 5회: ", s)  # __str__() 멤버 함수 호출
print(" push 5회: ", s.array)
