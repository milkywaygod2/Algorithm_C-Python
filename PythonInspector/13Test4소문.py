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
'''

import heapq

def spoil_rumor(graph, x):
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