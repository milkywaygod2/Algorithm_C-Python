'''
graph가 주어질 때, 간선의 가중치가 c 이상인 신장 트리 중 그 가중치가 최소가 되는 신장트리의 가중치의 합을 반환하는 함수를 작성하세요.

가짜 최소신장트리
그래프가 주어질 때, 그 최소신장트리란 모든 정점을 잇는 트리 중에서 그 가중치의 합이 가장 작은 트리를 말한다.
최소신장트리에 대하여 배우던 엘리스씨는, 너무 값이 작은 정점들만을 택하는 것에 대해서 재미가 없다고 생각하였다. 
이에 엘리스씨가 생각한 것은, 모든 정점을 잇는 트리 중에서 그 간선의 가중치가 모두 c보다 크거나 같은 트리 중에서 가중치의 합이 가장 작은 트리를 구하고 싶어 한다. 
즉, 가중치가 c보다 작은 간선은 해당 트리에 존재하면 안 된다. 이를 특이한 신장트리라고 하자.
엘리스씨를 도와 특이한 신장트리를 구하는 프로그램을 작성하시오. 만약 간선의 가중치가 모두 c보다 크거나 같은 신장트리가 존재하지 않는다면, -1을 출력한다.

입력
첫째 줄에는 정점의 개수, 간선의 개수, 그리고 특이한 신장트리의 간선의 가중치를 결정하는 상수 c가 주어집니다.
둘째 줄부터 간선의 정보가 주어집니다. 각 줄은 정수 a b c 로 구성되며, 이는 a와 b사이에 가중치 c인 간선이 존재한다는 의미입니다.

출력
최소 신장 트리의 간선 가중치의 합을 출력합니다.

입력 예시
8 11 2
0 1 3
0 5 1
1 2 1
1 3 4
1 5 3
2 4 2
2 7 4
2 6 1
3 4 3
4 6 4
6 7 2

출력 예시
21
'''

import sys
sys.setrecursionlimit(100000)

def getPseudoMST(graph, c) :

    return 0

#main.py
def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]
    c = line[2]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getPseudoMST(graph, c))

if __name__ == "__main__":
    main()
