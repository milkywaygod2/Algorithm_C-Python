'''
n*n크기의 땅, 각 칸은 1*1사이즈, 고유의 도달점수있음
(0,0)에서 출발, 맨 오른쪽 아래 (n-1,n-1)도착시 가능한 고득점이 목표
이동은 오른쪽, 아래쪽, 오른쪽 대각선 아래 방향으로 한 칸씩 3가지 경우만 가능
(i,j)에서 (i,j+1) (i+1,j) (i+1,j+1)
시작,도착점도 점수 획득가능

입력
첫째줄에 n입력됨 (3<=n<=300)
둘째줄부터 n개의 줄에 걸쳐 각줄마다 n개의 정수가 공백기준으로 구분되어 입력됨
이 정수들은 각 칸에 도착하였을때 얻는 점수를 의미 (-10000<=점수<=10000)

출력
도착점에서 가능한 가장 높은 점수는?

3
1 -2 -3
-4 5 6
7 8 9

23

3
1 -2 -3
-4 5 6
17 8 9

31
'''

def get_score(myMap):
    n = len(myMap)
    dp = [[-1e9]*n for _ in range(n)]  # dp[i][j]는 (i, j)까지 도달했을 때의 최대 점수
    dp[0][0] = myMap[0][0]  # 시작점의 점수

    # 각 위치에 대해
    for i in range(n):
        for j in range(n):
            # 오른쪽으로 이동
            if j+1 < n:
                #큰음수초기화값vs시작점기저+myMap입력값
                dp[i][j+1] = max(dp[i][j+1], dp[i][j] + myMap[i][j+1]) 
            # 아래로 이동
            if i+1 < n:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + myMap[i+1][j])
            # 대각선으로 이동
            if i+1 < n and j+1 < n:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + myMap[i+1][j+1])

    return dp[-1][-1]  # 도착점의 최대 점수 반환

def main():
    '''
    테스트를 위한 코드입니다.
    '''
    
    n = int(input())
    
    myMap = []
    
    for j in range(n) :
        line = [ int(v) for v in input().split() ]
        myMap.append(line)
        
    result = get_score(myMap)
    
    print(result)

if __name__ == '__main__':
    main()
