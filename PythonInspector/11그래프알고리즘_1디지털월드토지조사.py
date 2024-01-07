'''
�Է�
ù° �ٿ��� ������ ������ ũ�Ⱑ �־����ϴ�. ������ ����� �׻� ���簢���Դϴ�. �� ��° �ٺ��� ������ ���� ������ ������ �־����ϴ�. 1�� ��, 0�� �ٴ��Դϴ�.

���
1�� ��,��,��,��� ����Ǿ��ִ� ��츦 ���̶�� �մϴ�.
�ΰ��� ������ ���� Ʃ���� ����մϴ�. (���� ��ü ����, �� ���� ũ�⸦ ������������ ������ ����Ʈ)�� ����մϴ�.

�����п����� ������ ����� �־����� ��, ���� ���� (int) �� �� ���� ũ��� (list)�� ��ȯ�ϼ���.
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

(3, [7, 8, 9])
'''
isize = 0

def dfs(x,y,pMap,visited):
    visited[x][y] = 1 #�湮ó��

    global isize
    dir = [(1,0), (0,1), (-1,0), (0,-1)]
    n = len(pMap)

    for d in dir:
        nx = x+d[0]
        ny = y+d[1]

        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: continue
        if pMap[nx][ny] == 0: continue
        if not visited[nx][ny]:
            isize += 1
            dfs(nx,ny,pMap,visited)


def cadastralSurvey(pMap):
    global isize
    island_cnt = 0
    n = len(pMap)
    visited = []
    for i in range(n):
        visited.append([0 for j in range(n)])

    island_size = []
    for i in range(n):
        for j in range(n):
            if pMap[i][j] == 1 and visited[i][j] == 0:
                island_cnt += 1
                isize = 1
                dfs(i,j,pMap, visited)
                island_size.append(isize)

    island_size.sort()
    return island_cnt, island_size


def read_input():
    size = int(input())
    returnMap = []
    for i in range(size):
        line = input()
        __line = []
        for j in range(len(line)) :
            __line.append(int(line[j]))
        
        returnMap.append(__line)
    return returnMap

def main():
    pMap = read_input()
    print(cadastralSurvey(pMap))

if __name__ == "__main__":
    main()

