"""
날짜: 2025-10-01
이름: 박용성
프로그램명: 후위표식 계산기 구현
프로그램 설명: 클래스를 이용한 리스트 기반 후위표식 계산기 구현
"""

from ArrayStack import ArrayStack


def evalPostfix(expr):
    s = ArrayStack(100)

    for token in expr:
        if token in "+-*/":  # 연산자인 경우
            val2 = s.pop()  # 피연산자2
            val1 = s.pop()  # 피연산자1
            if token == "+":
                s.push(val1 + val2)
            elif token == "-":
                s.push(val1 - val2)
            elif token == "*":
                s.push(val1 * val2)
            elif token == "/":
                s.push(val1 / val2)
        else:  # 피연산자인 경우
            s.push(float(token))

    return s.pop()


expr1 = ["8", "2", "/", "3", "-", "3", "2", "*", "+"]
expr2 = ["1", "2", "/", "4", "*", "1", "4", "/", "*"]

print(evalPostfix(expr1))
print(evalPostfix(expr2))
