'''
숫자 만들기
1부터 3까지의 수를 더하여 5을 만드는 경우의 수는 다음과 같이 13가지가 존재합니다.
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 2 + 1
1 + 2 + 1 + 1
2 + 1 + 1 + 1
1 + 2 + 2
2 + 1 + 2
2 + 2 + 1
1 + 1 + 3
1 + 3 + 1
3 + 1 + 1
2 + 3
3 + 2
1부터 m까지의 수를 더하여 n을 만드는 경우의 수를 구하는 프로그램을 작성하세요. 
단, 경우의 수가 매우 커질 수 있으므로, 경우의 수를 1,000,000,007 로 나눈 나머지를 출력합니다.
5 3

13

1 ~ m 까지의 수를 더하여 n을 만드는 경우의 수를 1,000,000,007로 나눈 나머지를 반환하는 함수를 작성하세요. 단, 경우의 수가 매우 커질 수 있으므로, 경우의 수를 1,000,000,007 로 나눈 나머지를 출력합니다.
    sum1to3(5) 
    = sum1to3(5-1)+sum1to3(5-2)+sum1to3(5-3)+sum1to3(5-4)+sum1to3(5-5)
    = sum1to3(4)+sum1to3(3)+sum1to3(2)+sum1to3(1)+sum1to3(0)    
    = {sum1to3(4-1)+sum1to3(3-1)+sum1to3(2-1)+sum1to3(1-1)}   // sum1to3(4)
                  +{sum1to3(3-1)+sum1to3(2-1)+sum1to3(1-1)}   // sum1to3(3)
                               +{sum1to3(2-1)+sum1to3(1-1)}   // sum1to3(2)
                                             +sum1to3(1-1)    // sum1to3(1)
                                             +1기저           // sum1to3(0)
    =...중략
    
'''
def makeNumber(n, m) : #_for바텀업, 반복식
    #점화식 result[n] = 시그마(i=1~m)::result[n-i]

    resultArr4_eachCases = [1] #n=0 기저

    #★점화식의 N-1 + N-2 + ..각각은 각N에대해 한 차수 낮은 값들의 합으로 되어있음 
    #N-1 = (N-1)-1 + (N-1)-2.. 
    #N-2 = (N-2)-1 + (N-2)-2..
    #결국 1~n 각 점화식에 대해 n만큼 반복문
    for N in range(1,n+1): 

        #아래가 개별 점화식 부분
        sumDP_recursion = 0
        for i in range(1, min(N,m)+1): #1~m, 만들 수 N보다는 i가 작거나 같아야함,n-m에서 m이 더크면 음수가 되니까
            sumDP_recursion += resultArr4_eachCases[N-i]
        resultArr4_eachCases.append(sumDP_recursion%1000000007) #n 캐이스별로 배열로 저장
    return resultArr4_eachCases[n]


def makeNumber_recur(n, m) : #_recur탑다운, 재귀식

    resultArr4_eachCases = [1] #n=0 기저

    if not n in resultArr4_eachCases:
        #아래가 개별 점화식 부분
        sumDP_recursion = 0
        for i in range(1, min(n,m)+1): #1~m, 만들 수 N보다는 i가 작거나 같아야함
            sumDP_recursion += makeNumber_recur(n-i, m)
        resultArr4_eachCases[n] = sumDP_recursion%1000000007 #[n] 캐이스에 대해 재귀스택의 끝에서 기저인 [0]까지 가게됨
    return resultArr4_eachCases[n]


def main():
    '''
    아래 부분은 수정하지 마세요.
    '''

    firstLine = [int(x) for x in input().split()]

    n = firstLine[0]
    m = firstLine[1]

    print(makeNumber(n, m))

if __name__ == "__main__":
    main()
