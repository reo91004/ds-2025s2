"""
날짜: 2025-11-26
이름: 박용성
프로그램명: W13_6_TopologicalSort.py
프로그램 설명: 인접 행렬과 진입 차수를 이용한 위상 정렬 알고리즘
"""

def topological_sort_AM(vertex, edge):
    n = len(vertex)
    inDeg = [0] * n  # 진입차수 저장
    
    # 1. 모든 정점의 진입 차수 계산
    for i in range(n):
        for j in range(n):
            if edge[i][j] > 0:
                inDeg[j] += 1
    
    # 2. 진입 차수가 0인 정점을 리스트(스택처럼 사용)에 추가
    vlist = []
    for i in range(n):
        if inDeg[i] == 0:
            vlist.append(i)
            
    # 3. vlist가 빌 때까지 반복
    while len(vlist) > 0:
        v = vlist.pop() # 하나 꺼내서
        print(vertex[v], end=' ') # 출력
        
        # 꺼낸 정점(v)과 연결된 모든 정점(u)의 진입 차수 감소
        for u in range(n):
            if v != u and edge[v][u] > 0:
                inDeg[u] -= 1
                if inDeg[u] == 0: # 진입 차수가 0이 되면 리스트에 추가
                    vlist.append(u)

# --- 테스트 프로그램 ---
vertex = ['A', 'B', 'C', 'D', 'E', 'F']
graphAM = [
    [0, 0, 1, 1, 0, 0], # A -> C, D
    [0, 0, 0, 1, 1, 0], # B -> D, E
    [0, 0, 0, 1, 0, 1], # C -> D, F
    [0, 0, 0, 0, 0, 1], # D -> F
    [0, 0, 0, 0, 0, 1], # E -> F
    [0, 0, 0, 0, 0, 0]  # F
]

print('topological_sort: ')
topological_sort_AM(vertex, graphAM)
print()