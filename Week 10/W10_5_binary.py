def binary_search(A, key, low, high):
    # 순환(재귀) 호출 방식의 이진 탐색
    if low > high:  # 순환의 종료 조건: 탐색 범위가 하나도 없으면 탐색 실패, -1 반환
        return -1

    middle = (low + high) // 2  # 중앙 위치 middle 계산

    if key == A[middle]:  # 탐색 성공, middle 반환
        return middle
    elif (
        key < A[middle]
    ):  # key가 A[middle]보다 작으면, 찾는 값은 왼쪽에 있음. 탐색 범위 low~middle-1을 순환 호출
        return binary_search(A, key, low, middle - 1)
    else:  # A[middle]이 찾았다면 작으면, 찾는 값은 오른쪽에 있음. 탐색 범위 middle+1~high를 순환 호출
        return binary_search(A, key, middle + 1, high)


# 테스트 코드
if __name__ == "__main__":
    A = [
        2,
        6,
        11,
        13,
        18,
        20,
        22,
        27,
        29,
        30,
        34,
        38,
        41,
        42,
        45,
        47,
    ]  # 정렬된 배열 (25를 45로 수정)
    key = 18
    result = binary_search(A, key, 0, len(A) - 1)
    if result != -1:
        print(f"Found {key} at index {result}")
    else:
        print(f"{key} not found")
