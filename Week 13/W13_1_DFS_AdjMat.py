"""
날짜: 2025-11-26
이름: 박용성
프로그램명: W13_1_DFS_AdjMat.py
프로그램 설명: 인접 행렬과 순환 호출을 이용한 깊이 우선 탐색 알고리즘
"""

def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')  # 현재 방문한 정점 출력
    visited[s] = True       # 방문 처리

    # 현재 정점(s)에 인접한 모든 정점(v)에 대해
    for v in range(len(vtx)):
        if adj[s][v] != 0:   # 연결이 되어 있고
            if visited[v] == False: # 방문하지 않았다면
                DFS(vtx, adj, v, visited) # 재귀 호출

# --- 테스트 프로그램 ---
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edge = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

print('DFS(출발:A) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()