'''
�Է�
ù ��° �ٿ� ���ڿ� s1, �� ��° �ٿ� ���ڿ� s2�� �־�����. �� ���̴� 1000�� ���� �ʴ´�.

���
�ִ� ���� �κ� ������ ���̸� ����Ѵ�.

���ڿ� s1, s2�� �ִ� ���� �κ� ������ ���̸� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
Television
Telephone

6

���1: i == 0 | j == 0 ������ �� ��� 
���2: s1[i] == s2[j] ���� ���
���3: s1[i] != s2[j] �ٸ� ���
'''

def LCS(s1, s2) :
    m = len(s1)
    n = len(s2)
    L = [[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: #�ݺ����������� �ε������� ����
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[m][n]

import sys

def main():
    '''
    �� �κ��� �������� ������.
    '''

    s1 = input()
    s2 = input()

    print(LCS(s1, s2))

if __name__ == "__main__":
    main()
