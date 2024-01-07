#���ͽ�Ʈ�� : ���� ����ġ�� ����
#�������� : ���Ұ��(���ǰ���ġ)

'''
�Է�
ù° �ٿ��� ������ ����, ������ ����, �������� ���� ��ȣ, �׸��� �������� ���� ��ȣ�� �־����ϴ�.
��° �ٺ��� ������ ������ �־����ϴ�. �� ���� ���� a b c �� �����Ǹ�, �̴� a�� b���̿� ����ġ c�� ������ �����Ѵٴ� �ǹ��Դϴ�.

���
���������� ������������ �ִܰŸ��� ����մϴ�.

graph�� �־��� ��, start���� end������ �ִܰŸ��� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
8 11 0 6
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

13
'''

import sys
sys.setrecursionlimit(100000)

def getShortest(graph, start, end) :
    V = len(graph)
    dist = [float('inf') for i in range(V)]
    visited = [False for i in range(V)]

    dist[start] = 0

    while True:
        mini = float('inf')
        node = 1
        for j in range(V):
            if visited[j] == False and dist[j] < mini:
                mini = dist[j]
                node = j
        if mini == float('inf'):
            break

        visited[node] = True

        for j in range(len(graph[node])):
            des = graph[node][j][0]
            cost = graph[node][j][1]

            if dist[des] > dist[node] + cost:
                dist[des] = dist[node] + cost
    return dist[end]


def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]
    start = line[2]
    end = line[3]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getShortest(graph, start, end))

if __name__ == "__main__":
    main()
