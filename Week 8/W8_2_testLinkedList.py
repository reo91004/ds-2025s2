"""
날짜: 2025-10-22
이름: 박용성
프로그램명: LinkedList
프로그램 설명: 연결리스트로 리스트 구현하기
"""

from LinkedList import LinkedList

L = LinkedList()
print("최초 : ", L)
L.insert(0, 10)
L.insert(0, 20)
L.insert(1, 30)
L.insert(3, 40)
L.insert(2, 50)
print("삽입 후 : ", L)
L.delete(2)
print("삭제 후(2) : ", L)
L.delete(3)
print("삭제 후(3) : ", L)
L.delete(0)
print("삭제 후(0) : ", L)
