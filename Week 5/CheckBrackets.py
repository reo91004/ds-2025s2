"""
날짜: 2025-10-01
이름: 박용성
프로그램명: CheckBrackets 구현
프로그램 설명: 괄호 검사 프로그램 구현
"""

from ArrayStack import ArrayStack


def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch == "(" or ch == "[" or ch == "{":
            stack.push(ch)

        elif ch == ")" or ch == "]" or ch == "}":
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (
                    (ch == ")" and left != "(")
                    or (ch == "]" and left != "[")
                    or (ch == "}" and left != "{")
                ):
                    return False

    return stack.isEmpty()


filename = "ArrayStack.h"
infile = open(filename, "r", encoding="euc-kr")
str = infile.read()
infile.close()

print("소스파일:", filename, " ---> ", checkBrackets(str))

filename = "ArrayStack.h"
with open(filename, "r", encoding="euc-kr") as infile:
    str = infile.read()
    print("소스파일:", filename, " ---> ", checkBrackets(str))
