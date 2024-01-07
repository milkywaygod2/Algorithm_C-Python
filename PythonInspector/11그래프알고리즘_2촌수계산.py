'''
�Է�
ù° �ٿ��� ����� �� (N)�� ģ�������� �� (M)�� �־����ϴ�.
��° �ٿ��� �̼��� �˰� ���� �� ������� ��ȣ�� �־����ϴ�. �� ������� ��ȣ�� 0�̻� N�̸��Դϴ�.
��° �� ���� M���� ģ�����谡 �� ������� ��ȣ�� �־����ϴ�. ģ�����踦 ��Ÿ�� ��, a b�� b a�� ������ �����Դϴ�.

���
�� ������� �̼��� ����մϴ�. ���� ģ�����谡 �ƴ϶�� -1�� ����մϴ�

������ģ���� ģ�����谡 myInput���� �־�����, ����� a, b�� �־��� �� �� ������ �̼��� ��ȯ�մϴ�.
5 5
0 4
0 1
0 2
1 3
2 3
3 4

3

5 0
0 2

-1
'''

import sys
from collections import deque
sys.setrecursionlimit(100000)

def SNS(n_nodes, myInput, a, b):
    if a == b: return 0

    graph = [ [] for i in range(n_nodes) ]
    m_edges = len(myInput)

    for line in myInput:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    queue = deque([a])
    visit = [0] * n_nodes
    visit[a] = 1

    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if visit[node] == 0:
                visit[node] = visit[cur]+1
                queue.append(node)

    #�����ʿ�, �ڱ��ڽ��� 0��
    return visit[b]-1 if visit[b] > 0 else -1 #else: �ƹ����谡 ���� ���


from collections import deque
def main():
    '''
    �Ʒ� �ڵ带 �������� ���ÿ�.
    '''
    
    n_nodes, m_edges = input().split()
    n_nodes = int(n_nodes)
    m_edges = int(m_edges)
    
    a, b = input().split()
    a = int(a)
    b = int(b)

    myInput = []

    for i in range(m_edges) :
        line = [int(x) for x in input().split()]
        myInput.append(line)
    
    print(SNS(n_nodes,myInput,a,b))

if __name__ == "__main__":
    main()
