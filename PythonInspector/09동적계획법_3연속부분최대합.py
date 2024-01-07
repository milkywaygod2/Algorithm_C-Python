'''
1.목표: maxSum(n) = n번째 숫자로 끝나는(오른쪽끝) 연속부분최대합
2.부분문제점화식: 
두가지경우
maxSum(n-1)에 현재n번째 값을 포함하기 (기존에 하나더) //maxSum(n-1) + arr(n)
n번째부터 새롭게 연속합을 시작하기 (새로운 조합) //0 + arr(n)
maxSum(n) = max(maxSum(n-1),0) + arr(n)

연속부분최대합
1 2 -4 5 3 -2 9 -10
15
'''

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 
    그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    maxSum = []
    final_max = data[0]
    maxSum.append(data[0])

    for n in range(1,len(data)):
        maxSum.append(max(maxSum[n-1],0) + data[n])
        if final_max < maxSum[n]:
            final_max = maxSum[n]    
    
    return final_max

def getSubsum_recur(data): #???
    n = len(data)
    maxSum = [None]*n
    final_max = data[0]
    maxSum.append(data[0])

    if maxSum[n] is not None:
        return maxSum[n]
    else:
        maxSum.append(max(maxSum[n-1],0) + data[n])



import sys

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
