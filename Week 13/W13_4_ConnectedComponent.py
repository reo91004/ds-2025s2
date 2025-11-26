"""
날짜: 2025-11-26
이름: 박용성
프로그램명: W13_4_ConnectedComponent.py
프로그램 설명: BFS를 이용한 그래프의 연결 성분 검사 알고리즘
"""

from queue import Queue

# 연결 성분 하나를 탐색하는 BFS 함수
def bfs_cc(vtx, adj, s, visited):
    group = [s]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    
    while not Q.empty():
        s = Q.get()
        for v in range(len(vtx)):
            if visited[v] == False and adj[s][v] != 0:
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group

# 전체 그래프의 연결 성분을 찾는 함수
def find_connected_component(vtx, adj):
    n = len(vtx)
    visited = [False]*n
    groups = []
    
    for v in range(n):
        if visited[v] == False:
            color = bfs_cc(vtx, adj, v, visited)
            groups.append(color)
            
    return groups

# --- 테스트 프로그램 ---
vertex = ['A', 'B', 'C', 'D', 'E']
adjMat = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

colorGroup = find_connected_component(vertex, adjMat)
print("연결성분 개수 = %d " % len(colorGroup))
print(colorGroup)