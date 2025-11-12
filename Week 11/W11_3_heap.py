"""
날짜: 2025-11-12
이름: 박용성
프로그램명: 최대 힙 구현
프로그램 설명: 최대 힙 자료구조의 기본 연산 구현
"""


def heappush(heap, n):
    """최대 힙에 원소 n 삽입"""
    heap.append(n)  # 맨 뒤에 임시로 추가
    i = len(heap) - 1  # 현재 위치(마지막 인덱스)

    # while i != 1 :  # 루트(인덱스 1)가 될 때까지 위로 올리기
    while i != 1:
        pi = i // 2  # 부모 인덱스
        if n <= heap[pi]:  # 부모가 더 크거나 같으면 중단
            break
        heap[i] = heap[pi]  # 부모를 끌어내림(한 칸 아래)
        i = pi  # 위로 이동
    heap[i] = n  # 알맞은 자리에 n 배치


def heappop(heap):
    """최대 힙에서 최댓값(루트) 제거 후 반환"""
    size = len(heap) - 1
    if size == 0:  # 빈 힙
        return None

    pi = 1  # 부모 인덱스(루트에서 시작)
    i = 2  # 자식 인덱스(왼쪽부터)
    root = heap[1]  # 반환할 최댓값(루트)
    last = heap[size]  # 마지막 원소(맨 아래-오른쪽)

    # 아래로 내려가며 last가 들어갈 자리를 찾는다
    while i <= size:
        # 두 자식 중 더 큰 자식을 고른다
        if i < size and heap[i] < heap[i + 1]:
            i += 1
        # last가 더 크거나 같으면 그 자리에 배치 가능 → 중단
        if last >= heap[i]:
            break
        heap[pi] = heap[i]  # 더 큰 자식을 끌어올림(한 칸 위)
        pi = i
        i *= 2  # 다음 레벨로 이동

    heap[pi] = last  # 찾은 자리에 last 배치
    heap.pop()  # 맨 뒤 원소 제거(중복 방지)
    return root


# ==========================================
# 테스트 프로그램
# ==========================================
if __name__ == "__main__":
    data = [2, 5, 4, 8, 9, 3, 7, 3]
    heap = [0]  # 0번 인덱스는 사용하지 않음

    print("입력: ", data)
    for e in data:
        heappush(heap, e)
        print("heap: ", heap[1:])  # 0번 항목을 제외하고 출력

    print("삭제: ", heappop(heap))
    print("heap: ", heap[1:])

    print("삭제: ", heappop(heap))
    print("heap: ", heap[1:])
