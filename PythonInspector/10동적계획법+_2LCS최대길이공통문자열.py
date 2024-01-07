'''
입력
첫 번째 줄에 문자열 s1, 두 번째 줄에 문자열 s2가 주어진다. 각 길이는 1000을 넘지 않는다.

출력
최대 공통 부분 수열의 길이를 출력한다.

문자열 s1, s2의 최대 공통 부분 수열의 길이를 반환하는 함수를 작성하세요.
Television
Telephone

6

경우1: i == 0 | j == 0 한쪽이 빈 경우 
경우2: s1[i] == s2[j] 같은 경우
경우3: s1[i] != s2[j] 다른 경우
'''

def LCS(s1, s2) :
    m = len(s1)
    n = len(s2)
    L = [[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: #반복문시퀸스와 인덱스차이 조정
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[m][n]

import sys

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    s1 = input()
    s2 = input()

    print(LCS(s1, s2))

if __name__ == "__main__":
    main()
