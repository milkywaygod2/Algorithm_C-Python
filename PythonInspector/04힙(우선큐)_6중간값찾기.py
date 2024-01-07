'''
중간값 찾기 : n개의 숫자가 차례대로 주어질 때, 매 순간마다 “지금까지 입력된 수 중에서 중간값”을 반환하는 프로그램을 작성하세요.
Max heap은 최대값에 바로 접근할 수 있다. + Min heap은 최소값에 바로 접근할 수 있다.
Heap의 두 성질을 이용하여, 중앙값보다 작은 값들은 Max heap에, 중앙값보다 큰 값들은 Min heap에 저장하는 방식으로 중앙값을 찾는 알고리즘을 구현할 수 있다.
- 1부터 99까지 숫자가 나열되었다있고 할때 중앙값이 50이면 1부터49는 최대힙, 51부터99까지는 최소힙으로 관리하고 하나 남을때는 최대힙(왼쪽)에 넣는다. 
- 최대힙루트값 < 최소힙루트값을 유지한다.(필요시교환)
==>노드수가 홀수라면 중간값은 최대힙의 루트값, 짝수개라면 두 루트의 중앙값이다.
입력
첫 번째 줄에 입력될 수의 개수를 나타내는 정수 n이 주어집니다. (2≤n≤150,000)
두 번째 줄에 n개의 정수가 공백으로 구분되어 입력됩니다.
입력되는 n개의 정수들을 x라고 할 때, −5,000≤x≤5,000을 만족합니다.

출력
n개의 정수가 차례대로 주어질 때, 매 순간마다의 중간값을 리스트로 담아 반환하는 find_mid 함수를 작성하세요.
입력된 수의 개수가 짝수라면 중간값이 2개입니다. 이러한 경우에는 더 작은 값을 저장하세요.
10
1 2 3 4 5 6 7 8 9 10

1 1 2 2 3 3 4 4 5 5

7
1 -2 -5 10 4 7 5

1 -2 -2 -2 1 1 4
'''

import heapq
def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    n = len(nums)
    result = []
    
    lmaxheap = []
    rminheap = []

    for i in range(n):
        x = nums[i]

        #둘 중에 하나라도 비었을때(초기단계) ==> 일단 왼쪽에 밀어넣어서 최대힙 정렬
        #어짜피 2개되면 아래 while not에서 나눠짐
        if not lmaxheap or not rminheap: 
            heapq.heappush(lmaxheap, -x)
        
        else: #양쪽에 최대/최소 힙이 모두 만들어졌을때
            if x >= -lmaxheap[0]: #최대힙 루트 보다 크거나(당연) 같으면(균형) 오른쪽으로 가시오~
                heapq.heappush(rminheap, x)
            else:
                heapq.heappush(lmaxheap, -x)

        #힙크기조정
        #자료개수 조건 왼쪽 최대힙이 1개 더 많거나 같아야함
        while not (len(lmaxheap)-len(rminheap) == 0 or len(lmaxheap)-len(rminheap) == 1):
            if len(lmaxheap) > len(rminheap): #l이 r보다 2개이상 많음
                heapq.heappush(rminheap, -heapq.heappop(lmaxheap))
            else: #r이 l보다 1개이상 많음
                heapq.heappush(lmaxheap, -heapq.heappop(rminheap))

        result.append(-lmaxheap[0])

    return result


def main():
    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())
    
    nums = [int(v) for v in input().split()]
    
    print(*find_mid(nums))
                    
if __name__ == "__main__":
    main()
