"""
날짜: 2025-11-26
이름: 박용성
프로그램명: W13_5_SpanningTree.py
프로그램 설명: DFS를 이용하여 그래프의 신장 트리를 구하는 알고리즘
"""

def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end=' ')
                ST_DFS(vtx, adj, v, visited)

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
    [0, 0, 0, 0, 1, 0, 1, 0]
]

print('신장트리(DFS): ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()