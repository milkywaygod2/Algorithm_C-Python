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

÷�ε帰 �ڵ�� ���ͽ�Ʈ�� �˰����� ����Ͽ� �׷����� �� ���� �� �ִ� ��θ� ����ϰ�, ���� ���������� �ҹ��� ���� ������ ��ȣ�� ��ȯ�ϴ� �Լ��Դϴ�.

�Ʒ� ������ �ڵ��� �ֿ� �κп� ���� �����Դϴ�.

�ʱ�ȭ: ����, �ڵ�� �׷����� ��� ���� n�� �����ϰ�, �ִ� �Ÿ��� ������ Table�� �湮 ���θ� ��Ÿ�� check �迭�� �ʱ�ȭ�մϴ�. ���� ��� start���� ����ϹǷ�, Table[start]�� 0���� �ʱ�ȭ�մϴ�.
���ͽ�Ʈ�� �˰��� ����: for i in range(n): ���� ��� ��带 ��ȸ�ϸ鼭 �ִ� �Ÿ��� ����ϴ� ������ ��Ÿ���ϴ�. �ܺ� ���������� �� n�� �ݺ��˴ϴ�.
��������� �ִ� �Ÿ� �� �ּڰ� ã��: ���� ���������� ���� �湮���� ���� ��� �� �ִ� �Ÿ��� ���� ��带 ã���ϴ�. myMin�� myMinIdx ������ �ִ� �Ÿ��� �� ���� ��� �ε����� �����մϴ�.
�ִ� �Ÿ� ��� �湮 ó��: �ִ� �Ÿ��� ���� ��带 ã�� �Ŀ��� �ش� ��带 �湮 ó���ϰ�, �������ʹ� �� ��带 ���� �� �� �ִ� �ٸ� ������ �ִ� �Ÿ��� ������Ʈ�մϴ�.
������Ʈ�� �ִ� �Ÿ��� ���̺� ����: ���� ��忡�� �� �� �ִ� ��� ��忡 ����, ��������� �ִ� �Ÿ����� �� ª�� ��ΰ� �ִٸ� �ش� ��η� ������Ʈ�մϴ�.
�ִ� �ҹ� ���� ���� ã��: ����������, �� ����� �ִ� �Ÿ� �� �ִ��� ã�� �ش� ����� �ε����� ��ȯ�մϴ�.
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