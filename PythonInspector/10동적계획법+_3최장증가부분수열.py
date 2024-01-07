#LIS(n) = max(LIS(i)+1, arr[i]<arr[n] {i=0,1,2,...,n-1}
             
'''
수열이 list로 주어질 때, 최장 증가 부분 수열의 길이를 반환하는 함수를 작성하세요.
1 4 2 3 5

4
'''
#점화식 L[n] = max( L[i]+1 ) if (myData[n] > myData[i] && i < n )
def LIS(myData) :
    L = [0] * len(myData)
    for n in range(len(myData)):
        for i in range(n):
            if myData[i] < myData[n]:
                L[n] = max(L[n], L[i] + 1)


    return max(L)+1 #자기자신 초기화=0으로 해준것을 보정

#???
def LIS_recur(n):
    if n == 0: return 0
    if n not in memo:
        for i in range(0,n):
            if arr[i] < arr[n]:
                memo[n] = max(LIS(i))+1
    return memo[n]

import sys

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(v) for v in input().split()]

    print(LIS(data))

if __name__ == "__main__":
    main()
