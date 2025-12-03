"""
날짜: 2025-12-03
이름: 박용성
프로그램명: W14_1_matrix.py
프로그램 설명: 인접 행렬과 인접 리스트를 이용한 그래프 표현
"""

vertex = ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,   29,   None,   None,   None,   10,   None],
           [29,   None,   16,   None,   None,   None,   15  ],
           [None,   16,   None,   12,   None,   None,   None],
           [None,   None,   12,   None,   22,   None,   18  ],
           [None,   None,   None,   22,   None,   27,   25  ],
           [10,   None,   None,   None,   27,   None,   None],
           [None,   15,   None,   18,   25,   None,   None]]

def weightSum( vlist, W ):              # 매개변수: 정점 리스트, 인접 행렬
    sum = 0                             # 가중치의 합
    for i in range(len(vlist)) :        # 모든 정점에 대해(i: 0, ... N-1)
        for j in range(i+1, len(vlist)) : # 하나의 행에 대해 (삼각영역)
            if W[i][j] != None :        # 만약 간선이 있으면
                sum += W[i][j]          # sum에 추가
    return sum                          # 전체 가중치 합을 반환

def printAllEdges(vlist, W ):
    for i in range(len(vlist)) :
        for j in range(i+1, len(W[i])) :      # 모든 간선 W[i][j]에 대해
            if W[i][j] != None and W[i][j] != 0 :  # 간선이 있으면
                print("(%s,%s,%d)"%(vlist[i],vlist[j],W[i][j]), end=' ')
    print()


print('AM : weight sum = ', weightSum(vertex, weight))
printAllEdges(vertex, weight)


# 딕셔너리, 집합, 튜플, 리스트를 이용한 그래프 표현
graph ={'A' : {('B',29),('F',10)        },
        'B' : {('A',29),('C',16), ('G',15)},
        'C' : {('B',16),('D',12)        },
        'D' : {('C',12),('E',22), ('G',18)},
        'E' : {('D',22),('F',27), ('G',25)},
        'F' : {('A',10),('E',27)        },
        'G' : {('B',15),('D',18), ('E',25)} }

# 인접 리스트에서의 가중치의 합 계산
def weightSum(graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]
    return sum//2

# 인접 리스트에서의 모든 간선 출력
def printAllEdges(graph):
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)"%(v,e[0],e[1]), end=' ')

# 실행 코드
print("AL : weight sum = ", weightSum(graph))
printAllEdges(graph)