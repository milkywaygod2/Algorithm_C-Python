'''
���ͽ�Ʈ�� �׷��� �˰���
graph : n���� ���õ� ���̿� ����� ���ο� ���� ������ ��� �ִ� n*n ���� ���
x : �������� ���ʷ� �ҹ��� �۶߸� ������ ��ȣ

ù��° �ٿ� ���� n,m,x�� �Էµ�
n�� ���� ��(1<=n<=1000), 
m�� ���ó��� ����� ���� ��(1<=m<=5000), 
x�� ���� �ҹ��۶߸� ���ù�ȣ

�ι�° �ٺ��� m���� �ٿ� ���� ���� ���� a,b,c�� �Էµ�
a�� b���� ������ ���ΰŸ��� c��(1<=c<=1000)

���
n�����ÿ� �ҹ��� �۶߷�����, ���� �������� �ҹ��� ������ ���ù�ȣ ��ȯ.
'''

import heapq

def spoil_rumor(graph, x):
    INF = int(1e9) # ������ �ǹ��ϴ� ������ 10���� ����
    n = len(graph) # ������ ��
    distance = [INF] * n # �ִ� �Ÿ� ���̺��� ��� �������� �ʱ�ȭ

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start)) # ���� ���� ���� ���� �ִ� ��δ� 0���� �����Ͽ�, ť�� ����
        distance[start] = 0
        while q: # ť�� ������� �ʴٸ�
            dist, now = heapq.heappop(q) # ���� �ִ� �Ÿ��� ª�� ��忡 ���� ���� ������
            if distance[now] < dist: # ���� ��尡 �̹� ó���� ���� �ִ� ����� ����
                continue
            for i in graph[now]: # ���� ���� ����� �ٸ� ������ ������ Ȯ��
                cost = dist + i[1]
                if cost < distance[i[0]]: # ���� ��带 ���ļ�, �ٸ� ���� �̵��ϴ� �Ÿ��� �� ª�� ���
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(x) # ���ͽ�Ʈ�� �˰����� ����

    max_distance = max([d for d in distance if d != INF]) # ���� �������� �ҹ��� ������ ������ �ִ� �Ÿ�
    return distance.index(max_distance) # ���� �������� �ҹ��� ������ ���ù�ȣ ��ȯ