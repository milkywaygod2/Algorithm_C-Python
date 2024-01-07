#LIS(n) = max(LIS(i)+1, arr[i]<arr[n] {i=0,1,2,...,n-1}
             
'''
������ list�� �־��� ��, ���� ���� �κ� ������ ���̸� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
1 4 2 3 5

4
'''
#��ȭ�� L[n] = max( L[i]+1 ) if (myData[n] > myData[i] && i < n )
def LIS(myData) :
    L = [0] * len(myData)
    for n in range(len(myData)):
        for i in range(n):
            if myData[i] < myData[n]:
                L[n] = max(L[n], L[i] + 1)


    return max(L)+1 #�ڱ��ڽ� �ʱ�ȭ=0���� ���ذ��� ����

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
    �� �κ��� �������� ������.
    '''

    data = [int(v) for v in input().split()]

    print(LIS(data))

if __name__ == "__main__":
    main()
