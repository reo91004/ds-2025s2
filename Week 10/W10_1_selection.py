"""
날짜: 2025-11-05
이름: 박용성
프로그램명: 선택 정렬(Selection Sort)
프로그램 설명: 선택 정렬 알고리즘을 구현하고 각 단계별로 배열의 상태를 출력하는 프로그램
"""


def printStep(A, step):
    print(f"    Step {step}: {A}")


def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[least] > A[j]:
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i + 1)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original: ", data)
selection_sort(data)
print("Sorted: ", data)
