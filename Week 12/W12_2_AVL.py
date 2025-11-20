"""
날짜: 2025-11-19
이름: 박용성
프로그램명: W12_2_AVL.py
프로그램 설명: AVL 트리 구현
"""

from collections import deque

# =========================================================
# 1. 노드 클래스 및 기본 트리 연산 함수
# =========================================================
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# 트리의 높이 계산 (AVL 균형 인수 계산을 위해 필요)
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    return max(hLeft, hRight) + 1

# 균형 인수(Balance Factor) 계산 함수
def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right) # 왼쪽 높이 - 오른쪽 높이

# 노드 개수 계산
def count_node(n):
    if n is None:
        return 0
    return 1 + count_node(n.left) + count_node(n.right)

# 단말 노드 개수 계산 (테스트 프로그램용)
def count_leaf(n):
    if n is None:
        return 0
    if n.left is None and n.right is None:
        return 1
    return count_leaf(n.left) + count_leaf(n.right)

# =========================================================
# 2. AVL 트리 회전 연산 함수들
# =========================================================

# LL 회전
def rotateLL(A):
    B = A.left              # 시계방향 회전
    A.left = B.right
    B.right = A
    return B                # 새로운 루트 B를 반환

# RR 회전
def rotateRR(A):
    B = A.right             # 반 시계방향 회전
    A.right = B.left
    B.left = A
    return B                # 새로운 루트 B를 반환

# LR 회전 
def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)    # RR회전
    return rotateLL(A)      # LL회전

# RL 회전
def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)   # LL회전
    return rotateRR(A)      # RR회전

# =========================================================
# 3. AVL 트리 삽입 알고리즘
# =========================================================
def insert_avl(root, node):
    if root == None:
        return node

    if node.key == root.key:
        return root

    # root의 서브 트리에 node 삽입
    if node.key < root.key:
        root.left = insert_avl(root.left, node)
    elif node.key > root.key:
        root.right = insert_avl(root.right, node)
    
    # 이제 root에서 불균형이 발생할 수 있음
    bf = calc_height_diff(root)

    if bf > 1:
        if node.key < root.left.key:
            return rotateLL(root)
        else:
            return rotateLR(root)
            
    elif bf < -1:
        if node.key < root.right.key:
            return rotateRL(root)
        else:
            return rotateRR(root)
            
    return root

# =========================================================
# 4. 순회 함수
# =========================================================
def levelorder(root):
    if root is None:
        return
    
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n is not None:
            print(n.key, end=' ')
            queue.append(n.left)
            queue.append(n.right)

# =========================================================
# 5. 맵 클래스 정의 (BSTMap 상속 및 AVLMap 구현)
# =========================================================

# 부모 클래스: BSTMap (이전 단계의 기본 구현)
class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, value):
        return search_value_bst(self.root, value)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        self.root = insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg = 'BTSMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

# 자식 클래스: AVLMap
class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    def display(self, msg = 'AVLMap :'):
        print(msg, end='')
        levelorder(self.root)
        print()

# =========================================================
# 6. 테스트 프로그램
# =========================================================

# 데이터 셋
node = [7,8,9,2,1,5,3,6,4]
map = AVLMap()

for i in node:
    map.insert(i)
    map.display(f"AVL({i:d}): ")

print(f"노드의 개수 = {count_node(map.root)}")
print(f"단말의 개수 = {count_leaf(map.root)}")
print(f"트리의 높이 = {calc_height(map.root)}")