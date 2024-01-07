'''
입력
첫째 줄에는 디지털 월드의 크기가 주어집니다. 디지털 월드는 항상 정사각형입니다. 두 번째 줄부터 디지털 월드 국토의 정보가 주어집니다. 1은 땅, 0은 바다입니다.

출력
1이 상,하,좌,우로 연결되어있는 경우를 섬이라고 합니다.
두가지 정보를 가진 튜플을 출력합니다. (섬의 전체 갯수, 각 섬의 크기를 오름차순으로 정렬한 리스트)를 출력합니다.

디지털월드의 국토의 모양이 주어졌을 때, 섬의 갯수 (int) 와 각 섬의 크기들 (list)을 반환하세요.
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
    visited[x][y] = 1 #방문처리

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

