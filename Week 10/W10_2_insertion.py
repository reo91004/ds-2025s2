"""
날짜: 2025-11-05
이름: 박용성
프로그램명: 삽입 정렬(Insertion Sort)
프로그램 설명: 삽입 정렬 알고리즘을 구현하고 각 단계별로 배열의 상태를 출력하는 프로그램
"""


def printStep(A, step):
    print(f"    Step {step}: {A}")


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original: ", data)
insertion_sort(data)
print("Sorted: ", data)
