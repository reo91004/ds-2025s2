"""
날짜: 2025-10-01
이름: 박용성
프로그램명: ReverseString.py
설명: 사용자로부터 문자열을 입력받아 스택을 이용해 역순으로 출력
"""

from ArrayStack import ArrayStack


def reverseString(s):
    stack = ArrayStack(len(s))  # 문자열 길이만큼 스택 생성
    for ch in s:
        stack.push(ch)  # 한 글자씩 push

    result = ""
    while not stack.isEmpty():
        result += stack.pop()  # pop 하면서 역순 문자열 생성
    return result


# 실행
s = input("문자열 입력: ")
print("문자열 출력:", reverseString(s))
