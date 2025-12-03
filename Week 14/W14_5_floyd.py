"""
날짜: 2025-12-03
이름: 박용성
프로그램명: W14_5_floyd.py
프로그램 설명: 플로이드 알고리즘을 이용한 최단 경로 구현
"""

INF = 9999 

def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF ", end='')
            else:
                print("%4d "%A[i][j], end='')
        print("")

def shortest_path_floyd(vertex, adj) :
    vsize = len(vertex)
    
    # 인접 행렬 복사 (Deep Copy)
    # 2차원 리스트이므로 각 행을 개별적으로 복사해야 함
    A = list(adj)
    for i in range(vsize) :
        A[i] = list(adj[i])
        
    # Floyd 알고리즘 수행
    # k: 거쳐가는 정점, i: 시작 정점, j: 도착 정점
    for k in range(vsize) :
        for i in range(vsize) :
            for j in range(vsize) :
                # 거쳐가는 경로(k)가 더 짧으면 갱신
                if (A[i][k] + A[k][j] < A[i][j]) :
                    A[i][j] = A[i][k] + A[k][j]
                    
        # (선택사항) 단계별 결과를 보고 싶다면 주석 해제
        # printA(A) 
        
    printA(A) # 최종 결과 출력

if __name__ == "__main__":
    # 정점 리스트
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    # 초기 인접 행렬 (가중치)
    weight = [ [0,      7,      INF,    INF,    3,      10,     INF],
               [7,      0,      4,      10,     2,      6,      INF],
               [INF,    4,      0,      2,      INF,    INF,    INF],
               [INF,    10,     2,      0,      11,     9,      4  ],
               [3,      2,      INF,    11,     0,      13,     5  ],
               [10,     6,      INF,    9,      13,     0,      INF],
               [INF,    INF,    INF,    4,      5,      INF,    0  ] ]

    print("Shortest Path By Floyd's Algorithm")
    shortest_path_floyd(vertex, weight)