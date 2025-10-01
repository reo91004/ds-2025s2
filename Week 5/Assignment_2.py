"""
날짜: 2025-10-01
이름: 박용성
프로그램명: PalindromeCheck.py
설명: 스택을 이용해 문자열이 회문인지 판별
"""

from ArrayStack import ArrayStack


def isPalindrome(s):
    # 문자열 전처리: 소문자 변환 + 알파벳만 남기기
    s = "".join(ch.lower() for ch in s if ch.isalnum())

    stack = ArrayStack(len(s))
    for ch in s:
        stack.push(ch)  # 모든 문자 스택에 삽입

    # 스택에서 pop하면서 원래 문자열과 비교
    for ch in s:
        if ch != stack.pop():
            return False
    return True


# 실행
s = input("문자열 입력: ")
if isPalindrome(s):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
