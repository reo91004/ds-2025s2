"""
날짜: 2025-12-03
이름: 박용성
프로그램명: W14_4_dijkstra.py
프로그램 설명: 다익스트라 알고리즘을 이용한 최단 경로 구현
"""

# 초기 설정 및 알고리즘 구현
INF = 999  # 무한대를 의미하는 값 (이미지 기준 999)

# 최소 거리(dist)를 가진 정점을 선택하는 함수
def choose_vertex(dist, found):
    min = INF
    minpos = -1
    for i in range(len(dist)):
        # 아직 방문하지 않았고(found[i]==False), 거리가 가장 짧은 정점 선택
        if dist[i] < min and found[i] == False:
            min = dist[i]
            minpos = i
    return minpos

# 다익스트라 알고리즘 함수
def shortest_path_dijkstra(vertex, adj, start):
    vsize = len(vertex)
    dist = list(adj[start])  # 시작 정점에서 연결된 거리 정보로 초기화
    path = [start] * vsize   # 경로 저장을 위한 리스트 (초기값은 시작점)
    found= [False] * vsize   # 방문 여부 체크 리스트
    
    found[start] = True      # 시작 정점 방문 처리
    dist[start] = 0          # 시작 정점의 거리는 0
    
    for i in range(vsize):
        # 단계별 dist 배열 상태 출력 (디버깅용)
        print("Step%2d: "%(i+1), dist) 
        
        # 방문하지 않은 정점 중 가장 가까운 정점(u) 선택
        u = choose_vertex(dist, found)
        found[u] = True
        
        # 선택된 정점(u)을 거쳐서 가는 거리가 더 짧으면 dist 갱신 (Relaxation)
        for w in range(vsize):
            if not found[w]: # 아직 방문하지 않은 정점에 대해
                if (dist[u] + adj[u][w] < dist[w]): # 더 짧은 경로 발견 시
                    dist[w] = dist[u] + adj[u][w]   # 거리 갱신
                    path[w] = u                     # 경로 갱신 (이전 정점 기록)
                    
    return path

if __name__ == "__main__":
    # 정점 정의
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    # 인접 행렬 (가중치 그래프)
    # 0은 자기자신, INF는 연결없음
    weight = [ [0,   7,   INF, INF, 3,   10,  INF],
               [7,   0,   4,   10,  2,   6,   INF],
               [INF, 4,   0,   2,   INF, INF, INF],
               [INF, 10,  2,   0,   11,  9,   4  ],
               [3,   2,   INF, 11,  0,   13,  5  ],
               [10,  6,   INF, 9,   13,  0,   INF],
               [INF, INF, INF, 4,   5,   INF, 0  ]]

    print("Shortest Path By Dijkstra Algorithm")
    
    start = 0  # 시작 정점은 0번, 'A'로 선택
    path = shortest_path_dijkstra(vertex, weight, start)

    # 최종 경로 출력 코드 (역추적)
    for end in range(len(vertex)):
        if end != start:
            print("[최단경로: %s->%s] %s" % 
                  (vertex[start], vertex[end], vertex[end]), end='')
            
            # path 배열을 이용해 역순으로 경로 추적
            while (path[end] != start):
                print(" <- %s" % vertex[path[end]], end='')
                end = path[end]
            print(" <- %s" % vertex[path[end]])