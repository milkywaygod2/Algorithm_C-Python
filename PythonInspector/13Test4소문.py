'''
다익스트라 그래프 알고리즘
graph : n개의 도시들 사이에 연결된 도로에 대한 정보를 담고 있는 n*n 인접 행렬
x : 엘리스가 최초로 소문을 퍼뜨릴 도시의 번호

첫번째 줄에 정수 n,m,x가 입력됨
n은 도시 수(1<=n<=1000), 
m은 도시끼리 연결된 도로 수(1<=m<=5000), 
x는 최초 소문퍼뜨릴 도시번호

두번째 줄부터 m개의 줄에 걸쳐 도로 정보 a,b,c가 입력됨
a와 b도시 사이의 도로거리가 c임(1<=c<=1000)

출력
n번도시에 소문을 퍼뜨렸을때, 가장 마지막에 소문이 퍼지는 도시번호 반환.

첨부드린 코드는 다익스트라 알고리즘을 사용하여 그래프의 각 도시 간 최단 경로를 계산하고, 가장 마지막으로 소문이 퍼진 도시의 번호를 반환하는 함수입니다.

아래 설명은 코드의 주요 부분에 대한 설명입니다.

초기화: 먼저, 코드는 그래프의 노드 수를 n에 저장하고, 최단 거리를 저장할 Table과 방문 여부를 나타낼 check 배열을 초기화합니다. 시작 노드 start에서 출발하므로, Table[start]을 0으로 초기화합니다.
다익스트라 알고리즘 수행: for i in range(n): 문은 모든 노드를 순회하면서 최단 거리를 계산하는 과정을 나타냅니다. 외부 루프에서는 총 n번 반복됩니다.
현재까지의 최단 거리 중 최솟값 찾기: 내부 루프에서는 아직 방문하지 않은 노드 중 최단 거리를 가진 노드를 찾습니다. myMin과 myMinIdx 변수는 최단 거리와 그 때의 노드 인덱스를 저장합니다.
최단 거리 노드 방문 처리: 최단 거리를 가진 노드를 찾은 후에는 해당 노드를 방문 처리하고, 이제부터는 이 노드를 통해 갈 수 있는 다른 노드들의 최단 거리를 업데이트합니다.
업데이트된 최단 거리로 테이블 갱신: 현재 노드에서 갈 수 있는 모든 노드에 대해, 현재까지의 최단 거리보다 더 짧은 경로가 있다면 해당 경로로 업데이트합니다.
최대 소문 전파 도시 찾기: 최종적으로, 각 노드의 최단 거리 중 최댓값을 찾고 해당 노드의 인덱스를 반환합니다.
'''

def spoil_rumor(graph, start):
    n = len(graph)
 
    Table = [987987987 for _ in range(n)]
    check = [False for _ in range(n)]
 
    Table[start] = 0
 
    for i in range(n):
        myMin = 987987987
        myMinIdx = -1
 
        for j in range(n):
            if check[j] == False and Table[j] < myMin:
                myMin = Table[j]
                myMinIdx = j
 
        cur = myMinIdx
        check[cur] = True
 
        for j in range(len(graph[cur])):
            des = graph[cur][j][0]
            cost = graph[cur][j][1]
 
            if Table[des] > Table[cur] + cost:
                Table[des] = Table[cur] + cost
 
    myMax = -1
    result = -1
 
    for i in range(len(Table)):
        if myMax < Table[i]:
            myMax = Table[i]
            result = i
 
    return result


import heapq
def spoil_rumor_my(graph, x):
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    n = len(graph) # 도시의 수
    distance = [INF] * n # 최단 거리 테이블을 모두 무한으로 초기화

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        distance[start] = 0
        while q: # 큐가 비어있지 않다면
            dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
                continue
            for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
                cost = dist + i[1]
                if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(x) # 다익스트라 알고리즘을 수행

    max_distance = max([d for d in distance if d != INF]) # 가장 마지막에 소문이 퍼지는 도시의 최단 거리
    return distance.index(max_distance) # 가장 마지막에 소문이 퍼지는 도시번호 반환