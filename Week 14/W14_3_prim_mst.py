"""
날짜: 2025-12-03
이름: 박용성
프로그램명: W14_3_prim_mst.py
프로그램 설명: 프림 알고리즘을 이용한 최소 신장 트리 구현
"""

INF = 9999          # 가장 큰 가중치 (무한대)

def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize) :
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')

        for v in range(vsize) :
            if (adj[u][v] != None):
                if selected[v]==False and adj[u][v]< dist[v] :
                    dist[v] = adj[u][v]
    print()

if __name__ == "__main__":
    weight = [ [0,      29,     None,   None,   None,   10,     None],
               [29,     0,      16,     None,   None,   None,   15  ],
               [None,   16,     0,      12,     None,   None,   None],
               [None,   None,   12,     0,      22,     None,   18  ],
               [None,   None,   None,   22,     0,      27,     25  ],
               [10,     None,   None,   None,   27,     0,      None],
               [None,   15,     None,   18,     25,     None,   0   ]]
    
    vertex = ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]

    print("MST By Prim's Algorithm")
    MSTPrim(vertex, weight)