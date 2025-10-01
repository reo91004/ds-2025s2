"""
날짜: 2025-10-01
이름: 박용성
프로그램명: Infix2Postfix 구현
프로그램 설명: 중위 표현식을 후위 표현식으로 변환하는 프로그램 구현
"""

from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix


def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in "(":  # 여는 괄호일 경우
            s.push("(")

        elif term in ")":  # 닫는 괄호일 경우
            while not s.isEmpty():
                op = s.pop()
                if op == "(":
                    break
                else:
                    output.append(op)

        elif term in "+-*/":  # 연산자일 경우
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)

        else:  # 피연산자일 경우
            output.append(term)

    # 스택에 남은 연산자 모두 출력으로
    while not s.isEmpty():
        output.append(s.pop())

    return output


def precedence(op):  # 연산자 우선순위 함수
    if op == "(" or op == ")":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    else:
        return -1


infix1 = ["8", "/", "2", "-", "3", "+", "(", "3", "*", "2", ")"]
infix2 = ["1", "/", "2", "*", "4", "*", "(", "1", "/", "4", ")"]

postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)

result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)

print(" 중위표기: ", infix1)
print(" 후위표기: ", postfix1)
print(" 계산결과: ", result1, end="\n\n")

print(" 중위표기: ", infix2)
print(" 후위표기: ", postfix2)
print(" 계산결과: ", result2)
