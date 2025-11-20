"""
날짜: 2025-11-19
이름: 박용성
프로그램명: W12_1_binary.py
프로그램 설명: 이진 탐색 트리 구현
"""

# =========================================================
# 1. 노드 클래스 정의 
# =========================================================
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# =========================================================
# 2. 알고리즘 함수들 
# =========================================================

# 탐색 연산: 최대와 최소 노드 (반복 구조)
def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

# 탐색 연산: 키를 이용한 탐색 (순환 구조)
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

# 값을 이용한 탐색 (슬라이드: "모든 노드를 검사해야 함")
def search_value_bst(n, value):
    if n is None:
        return None
    if n.value == value:
        return n
    
    # 왼쪽 서브트리에서 먼저 찾기
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    
    # 없으면 오른쪽 서브트리에서 찾기
    return search_value_bst(n.right, value)

# 삽입 연산 알고리즘 (순환 구조)
def insert_bst(root, node):
    if root == None:            # 공백 노드에 도달하면, 이 위치에 삽입
        return node             # node를 반환(이 노드가 현재 root 위치에 감)

    if node.key == root.key:    # 동일한 키는 허용하지 않음
        return root             # root를 반환(root는 변화 없음)

    # root의 서브트리에 node 삽입. root 및 조상 노드들은 변화 없음
    if node.key < root.key:
        # 왼쪽 서브트리에 넣어야 하는 경우.
        # 왼쪽 자식을 루트로 삽입 연산을 순환 호출하고, 왼쪽 자식 갱신
        root.left = insert_bst(root.left, node)
    else:
        # 오른쪽 서브트리에 넣어야 하는 경우.
        # 오른쪽 자식을 루트로 삽입 연산을 순환 호출하고, 오른쪽 자식 갱신
        root.right = insert_bst(root.right, node)
        
    return root # root를 반환(root는 변화 없음)

# 삭제 연산 알고리즘
def delete_bst(root, key):
    if root == None:      # 공백 트리
        return root

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
        # key가 루트보다 작거나 크면, 해당 자식이 루트인 서브트리에서 삭제를 계속 진행함(순환호출 이용).
        # 이때, 자식이 변경될 수도 있으므로 반환된 값으로 자식을 갱신해야 함
    
    # key가 루트의 키와 같으면 root를 삭제
    else:
        # case1(단말 노드) 또는 case2(오른쪽 자식만 있는 경우)
        if root.left == None:
            return root.right   # 이제 root가 삭제됨. root.right가 삭제되는 root의 위치로 이동함
        
        # case2(왼쪽 자식만 있는 경우)
        if root.right == None:
            return root.left    # root가 삭제됨. root.left가 삭제되는 root의 위치로 이동함
            
        # case3(두 자식이 모두 있는 경우)
        succ = search_min_bst(root.right)           # ① 후계자를 찾고(오른쪽 서브트리 최소 노드)
        root.key = succ.key                         # ② 후계자의 데이터 (key와 value)를 복사하고
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key) # ③ 마지막으로, 후계자 삭제(오른쪽 서브트리에서 후계자 킷값을 가진 노드를 순환호출로 삭제)

    return root

# 중위 순회 (display 함수에서 사용하기 위해 구현)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

# =========================================================
# 3. 이진탐색트리를 이용한 맵 클래스 (BSTMap)
# =========================================================
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

# =========================================================
# 4. 테스트 프로그램 
# =========================================================

# 데이터 셋
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
value = ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

map = BSTMap()         # 새로운 맵 생성
map.display("[삽입 전] : ")

for i in range(len(data)):
    map.insert(data[i], value[i])   # 맵에 엔트리를 삽입하면서 트리의 구조 확인
    map.display(f"[삽입 {data[i]:2d}] : ")

print('[최대 키] : ', map.findMax().key)
print('[최소 키] : ', map.findMin().key)

# 탐색 성공이면 "성공", 아니면 "실패" 출력
print('[탐색 26] : ', '성공' if map.search(26) != None else '실패')
print('[탐색 25] : ', '성공' if map.search(25) != None else '실패')
print('[탐색 일팔]: ', '성공' if map.searchValue("일팔") != None else '실패')
print('[탐색 일칠]: ', '성공' if map.searchValue("일칠") != None else '실패')

map.delete(3)           # 삭제 case 1
map.display("[삭제  3] : ")

map.delete(68)          # 삭제 case 2
map.display("[삭제 68] : ")

map.delete(18)          # 삭제 case 3
map.display("[삭제 18] : ")

map.delete(35)          # 루트 노드 삭제
map.display("[삭제 35] : ")