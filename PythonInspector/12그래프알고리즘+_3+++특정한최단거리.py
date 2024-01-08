'''
특정한 최단거리
그래프와 시작점 s와, 도착점 e가 주어진다. 이제 엘리스씨는 시작점에서 도착점까지 최단경로로 가려 한다. 이 시작점은 사실 엘리스씨의 집이고, 도착점은 엘리스씨가 가고싶은 여행지이다.
엘리스씨는 여행을 혼자 가지 않고, 친구들을 여럿 데려가기로 했다. 친구는 2명(?)이며, 이 친구들은 각각 정점 f1,f2에 살고있다. 
따라서 엘리스씨는 정점 s에서 출발하여 f1과 f2를 거쳐 도착점 e로 가는 경로 중에서 최단경로를 찾고싶어 한다.
한 번 방문했던 정점 혹은 간선을 다시 방문해도 관계가 없다. 엘리스씨는 단지 친구들을 모두 데리고 여행지에 최대한 빨리 도착하고 싶어 할 뿐이다. 
엘리스씨를 도와 s에서 f1,f2를 거쳐 도착점 e로 가는 최단경로의 길이를 출력하는 프로그램을 작성하세요.

입력
첫째 줄에는 정점의 개수, 간선의 개수, 시작점의 정점 번호 s, 그리고 도착점의 정점 번호 e, 친구가 살고있는 정점 번호 f1,f2가 주어집니다.
둘째 줄부터 간선의 정보가 주어집니다. 각 줄은 정수 a b c 로 구성되며, 이는 a와 b사이에 가중치 c인 간선이 존재한다는 의미입니다.

출력
시작점에서 도착점까지의 최단거리를 출력합니다.

입력 예시
8 11 0 6 4 7
0 1 3
0 5 1
1 2 4
1 3 1
1 5 1
2 4 6
2 6 9
2 7 4
3 4 2
4 6 9
6 7 3

출력 예시
18

설명
0 -> 5 -> 1 -> 2 -> 4 -> 2 -> 7 -> 6 으로 움직여야 한다.
'''
import sys
sys.setrecursionlimit(100000)

def getSpecialShortest(graph, start, end, f1, f2) :
    '''
    graph가 주어질 때, start부터 end까지 갈 때 f1과 f2를 거치는 경로의 최단거리를 반환하는 함수를 작성하세요.
    '''

    return 0

#main.py
def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]
    start = line[2]
    end = line[3]
    f1 = line[4]
    f2 = line[5]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getSpecialShortest(graph, start, end, f1, f2))

if __name__ == "__main__":
    main()
