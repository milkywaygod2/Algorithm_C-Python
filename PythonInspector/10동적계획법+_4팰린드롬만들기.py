#펠린드롬: 거꾸로 해도 '형두형'
'''
문자열 data가 주어질 때, 이를 팰린드롬으로 만들기 위해 제거해야 하는 문자 개수의 최솟값을 반환하는 함수를 작성하세요.
abcfba

1
'''
#점화식 
# if (data[i] == data[j]) then p[i][j] = p[i+1][j-1] 
# if (data[i] != data[j]) then p[i][j] = min(p[i+1][j], p[i][j-1]) + 1 
def palindrome(data) :
    n = len(data)
    p = [[0]*n for i in range(n)] #초기화겸 기저조건

    #오른쪽끝두번째기준 바로오른쪽부터 오른쪽끝까지 탐색, 기준을 왼쪽끝까지 반복하며 완전탐색
    #오른쪽끝부터 찬찬히 탐색하기때문에 확장된 범위에 대해서 else를 통해 배열에 충분히 갱신 가능
    for i in range(n-2, -1, -1): #n-2(끝에서 두번째)부터 -1직전(0)까지
        for j in range(i+1, n): #i+1 시작점 다음부터 끝(n)까지
            if data[i] == data[j]:
                p[i][j] = p[i+1][j-1]
            else:
                p[i][j] = min(p[i+1][j], p[i][j-1]) + 1 #돌면서 p배열에 팰린드롬값 저장
    return p[0][len(data)-1]

import sys
def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    s = input()

    print(palindrome(s))

if __name__ == "__main__":
    main()
