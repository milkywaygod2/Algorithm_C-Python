'''
입력
첫째 줄에는 사용자 수 (N)와 친구관계의 수 (M)가 주어집니다.
둘째 줄에는 촌수를 알고 싶은 두 사용자의 번호가 주어집니다. 각 사용자의 번호는 0이상 N미만입니다.
셋째 줄 부터 M개의 친구관계가 두 사용자의 번호로 주어집니다. 친구관계를 나타낼 때, a b는 b a와 동일한 관계입니다.

출력
두 사용자의 촌수를 출력합니다. 만약 친구관계가 아니라면 -1을 출력합니다

엘리스친구의 친구관계가 myInput으로 주어지고, 사용자 a, b가 주어질 때 둘 사이의 촌수를 반환합니다.
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

    #조정필요, 자기자신은 0촌
    return visit[b]-1 if visit[b] > 0 else -1 #else: 아무관계가 없는 경우


from collections import deque
def main():
    '''
    아래 코드를 수정하지 마시오.
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
