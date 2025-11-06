def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return None


# 테스트 코드
if __name__ == "__main__":
    A = [2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 25, 47]
    key = 18
    result = sequential_search(A, key, 0, len(A) - 1)
    if result is not None:
        print(f"Found {key} at index {result}")
    else:
        print(f"{key} not found")
