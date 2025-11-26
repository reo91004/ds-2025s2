"""
날짜: 2025-11-26
이름: 박용성
프로그램명: W13_2_DFS_Dict.py
프로그램 설명: 딕셔너리와 집합을 이용한 그래프 표현 및 깊이 우선 탐색(DFS)
"""

def DFS2(graph, v, visited):
    if v not in visited:      # v가 방문되지 않았으면
        visited.add(v)        # visited 집합에 추가
        print(v, end=' ')     # 정점 출력
        
        # graph[v]는 인접 정점들의 집합, visited는 방문한 정점 집합
        # 차집합(-) 연산으로 방문하지 않은 인접 정점만 추출
        nbr = graph[v] - visited 
        
        for u in nbr:         # 인접 정점들에 대해
            DFS2(graph, u, visited) # 재귀 호출
''
# --- 테스트 프로그램 ---
mygraph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D", "E"},
    "D": {"B", "C", "F"},
    "E": {"C", "G", "H"},
    "F": {"D"},
    "G": {"E", "H"},
    "H": {"E", "G"}
}

print('DFS2(출발:A) : ', end="")
DFS2(mygraph, "A", set())
print()