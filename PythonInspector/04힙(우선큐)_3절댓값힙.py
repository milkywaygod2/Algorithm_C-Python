
'''
입력
첫 번째 줄에 힙이 수행할 명령의 수를 나타내는 정수 n을 입력합니다. (1≤n≤540000)
두 번째 줄부터 n개의 줄에 걸쳐 수행할 명령을 입력합니다. 명령의 종류는 다음과 같습니다.
0 x : 정수 x를 힙에 입력 (−540000 ≤ x ≤ 540000)
1 : 힙의 우선순위가 가장 높은 원소 제거
2 : 힙의 우선순위가 가장 높은 원소 조회

8
0 5
0 4
0 -4
0 2
2
1
2
1

2
-4
'''
import heapq
class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = []

    def push(self, value) :
        heapq.heappush(self.data, (abs(value),value)) #배열속의배열

    def pop(self) :
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self) :
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0][1] #배열속의배열 포인트!
   
def main():
    myPQ = PriorityQueue()

    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())
    
    for i in range(n) :
        line = [int(v) for v in input().split()]
        if line[0] == 0 :
            myPQ.push(line[1])
        elif line[0] == 1 :
            myPQ.pop()
        elif line[0] == 2 :
            print(myPQ.top())
            
if __name__ == "__main__":
    main()
