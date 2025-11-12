"""
날짜: 2025-11-12
이름: 박용성
프로그램명: 이진 트리 연산
프로그램 설명: 노드 개수, 단말 노드 개수, 트리 높이 계산
"""

from CircularQueue import CircularQueue

# ==========================================
# 이진 트리 연산: 순회, 노드 개수, 단말 노드 수, 트리 높이
# ==========================================


# 트리의 노드를 나타내는 클래스 정의
class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# ==========================================
# 순회 알고리즘 (Inorder / Preorder / Postorder)
# ==========================================
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)


def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)


def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")


# ==========================================
# 레벨 순회 알고리즘
# ==========================================
def levelorder(root):
    queue = CircularQueue(100)  # 큐 객체 초기화 (용량 100으로 지정)
    queue.enqueue(root)  # 최초에 큐에는 루트 노드만 들어 있음.
    while not queue.isEmpty():  # 큐가 공백 상태가 아닌 동안,
        n = queue.dequeue()  # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end=" ")  # 먼저 노드의 정보를 출력
            queue.enqueue(n.left)  # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)  # n의 오른쪽 자식 노드를 큐에 삽입


# ==========================================
# 노드 개수 계산
# ==========================================
def count_node(n):
    if n is None:  # n이 None이면 공백 트리 --> 0을 반환
        return 0
    else:  # 좌우 서브트리의 노드 수의 합 + 1을 반환 (순환 이용)
        return 1 + count_node(n.left) + count_node(n.right)


# ==========================================
# 단말 노드(leaf node)의 수 계산
# ==========================================
def count_leaf(n):
    if n is None:  # 공백 트리 --> 0을 반환
        return 0
    elif n.left is None and n.right is None:  # 단말 노드 --> 1을 반환
        return 1
    else:  # 비단말 노드: 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)


# ==========================================
# 트리의 높이 계산
# ==========================================
def calc_height(n):
    if n is None:  # 공백 트리 --> 0을 반환
        return 0
    hLeft = calc_height(n.left)  # 왼쪽 트리의 높이 --> hLeft
    hRight = calc_height(n.right)  # 오른쪽 트리의 높이 --> hRight
    if hLeft > hRight:  # 더 높은 높이에 1을 더해 반환
        return hLeft + 1
    else:
        return hRight + 1


# ==========================================
# 테스트 프로그램
# ==========================================
if __name__ == "__main__":
    # 트리 구조 생성
    d = TNode("D", None, None)
    e = TNode("E", None, None)
    b = TNode("B", d, e)
    f = TNode("F", None, None)
    c = TNode("C", f, None)
    root = TNode("A", b, c)

    # 순회 결과 출력
    print("\nIn-Order  : ", end="")
    inorder(root)
    print("\nPre-Order : ", end="")
    preorder(root)
    print("\nPost-Order: ", end="")
    postorder(root)
    print("\nLevel-Order: ", end="")
    levelorder(root)
    print()

    # 노드 개수, 단말 노드 수, 트리 높이 출력
    print("\n노드의 개수 = %d개" % count_node(root))
    print("단말의 개수 = %d개" % count_leaf(root))
    print("트리의 높이 = %d" % calc_height(root))
