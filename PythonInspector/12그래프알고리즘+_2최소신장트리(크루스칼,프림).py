#ũ�罺Į: �ּҺ�� ��� ������ �켱����
#����: Ʈ�� ���ٰ��ɹ������� �ּҺ�� ��� �켱����
'''
�Է�
ù° �ٿ��� ������ ����, ������ ������ �־����ϴ�.
��° �ٺ��� ������ ������ �־����ϴ�. �� ���� ���� a b c �� �����Ǹ�, �̴� a�� b���̿� ����ġ c�� ������ �����Ѵٴ� �ǹ��Դϴ�.

���
�ּ� ���� Ʈ���� ���� ����ġ�� ���� ����մϴ�.

graph�� �־��� ��, �� �ּ� ��� ����Ʈ���� ���� ����ġ�� ���� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
8 11
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

16
'''


import sys
sys.setrecursionlimit(100000)

def union_is_same_group(parent, a, b):
    a_parent = find(parent, a)
    b_parent = find(parent, b)

    if a_parent == b_parent:
        return True
    else:
        parent[b_parent] = a_parent
        return False

def find(parent, a):
    if parent[a] == a:
        return a
    else:
        return find(parent, parent[a])

def getMST(graph) :
    edges = []
    n = len(graph)

    for i in range(n):
        for j in range(len(graph[i])):
            neighbor = graph[i][j][0]
            cost = graph[i][j][1]

            edges.append([i, neighbor, cost])
    
    def getKey(a): return a[2]    
    edges.sort(key=getKey)
    m = len(edges)

    parent = [i for i in range(n)]
    result = 0
    for i in range(m):
        v1 = edges[i][0]
        v2 = edges[i][1]
        cost = edges[i][2]

        v1_parent = find(parent, v1)
        v2_parent = find(parent, v2)

        if union_is_same_group(parent, v1_parent, v2_parent) == False:
            result += cost


    return result


def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getMST(graph))

if __name__ == "__main__":
    main()
