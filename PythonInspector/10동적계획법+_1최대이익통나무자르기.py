'''
cutRod(n) = max(price[i] + cutRod(n-i)) for all i in {1..8}

통나무의 길이 N과 가격표가 dictionary로 주어질 때, 통나무를 잘라서 얻을 수 있는 최대 이익을 반환하세요.
예) 길이 1의 가격이 3일 때, myData[1] = 3
4 4     통나무길이 판매길이종류갯수
1 1     l길이당  p가격
2 20
3 33
4 36
'''
def cutRod(N, myData) : #반복, 상향식
    #점화식 maxValueRod[n] = max(price[l]+maxValueRod[n-1])
    maxValueRod = [0 for i in range(N+1)] #통나무길이만큼 초기화, []로 두고 .append해도됨
    for n in range(N+1):
        for l, p in myData.items(): #key-value로 가져옴
            if n >= l: #본체보다 더 크게 자를 수는 없음
                maxValueRod[n] = max(maxValueRod[n], p + maxValueRod[n-l])
    return maxValueRod[N]

#???
def cutRod_recur(N, myData) : #재귀, 하향식
    #점화식 maxValueRod[n] = max(price[l]+maxValueRod[n-1])
    if n <= 0:
        return 0
    
    if n not in memo:
        for i in range(1,9):
            memo[n] = max(memo[n], price[i] + cutRod_recur(n-i))
    return memo[n]

import sys

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    
    data = dict()
    N, M = input().split()
    N = int(N)
    M = int(M)
    
    for i in range(M):
        l, p = input().split()
        data[int(l)] = int(p)

    print(cutRod(N, data))

if __name__ == "__main__":
    main()
