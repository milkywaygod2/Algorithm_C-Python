'''
cutRod(n) = max(price[i] + cutRod(n-i)) for all i in {1..8}

�볪���� ���� N�� ����ǥ�� dictionary�� �־��� ��, �볪���� �߶� ���� �� �ִ� �ִ� ������ ��ȯ�ϼ���.
��) ���� 1�� ������ 3�� ��, myData[1] = 3
4 4     �볪������ �Ǹű�����������
1 1     l���̴�  p����
2 20
3 33
4 36
'''
def cutRod(N, myData) : #�ݺ�, �����
    #��ȭ�� maxValueRod[n] = max(price[l]+maxValueRod[n-1])
    maxValueRod = [0 for i in range(N+1)] #�볪�����̸�ŭ �ʱ�ȭ, []�� �ΰ� .append�ص���
    for n in range(N+1):
        for l, p in myData.items(): #key-value�� ������
            if n >= l: #��ü���� �� ũ�� �ڸ� ���� ����
                maxValueRod[n] = max(maxValueRod[n], p + maxValueRod[n-l])
    return maxValueRod[N]

#???
def cutRod_recur(N, myData) : #���, �����
    #��ȭ�� maxValueRod[n] = max(price[l]+maxValueRod[n-1])
    if n <= 0:
        return 0
    
    if n not in memo:
        for i in range(1,9):
            memo[n] = max(memo[n], price[i] + cutRod_recur(n-i))
    return memo[n]

import sys

def main():
    '''
    �� �κ��� �������� ������.
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
