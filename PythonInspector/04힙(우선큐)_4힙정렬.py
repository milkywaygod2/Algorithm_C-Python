'''
단, 우선순위 큐를 이용하여 구현하도록 합니다.

입력값
첫 번째 줄에 n개의 숫자가 공백으로 구분되어 주어집니다.
10 9 8 7 6 5 4 3 2 1

1 2 3 4 5 6 7 8 9 10
'''
'''
heapSort 함수를 구현하세요.
'''
import heapq                                #lib
class PriorityQueue:
    '''
    우선순위 큐를 (최소)힙으로 구현합니다
    '''

    def __init__(self) :                    
        self.data = []                      #

    def push(self, value) :                 
         heapq.heappush(self.data, value)  #

    def pop(self) :
        if len(self.data) > 0:              #
            heapq.heappop(self.data)        #

    def top(self) :
        if len(self.data) == 0:             #
            return -1                       #
        else:                               #
            return self.data[0]            #

def heapSort(items) :
    '''
    items에 있는 원소를 heap sort하여 리스트로 반환하는 함수를 작성하세요.

    단, 이전에 작성하였던 priorityQueue를 이용하세요.
    '''

    result = []
    pq = PriorityQueue() #최소힙
    for item in items:
        pq.push(item)
    
    for i in range(len(items)):
        result.append(pq.top())
        pq.pop() #맨뒤에껄 앞으로 올리고 정렬까지

    return result

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    print(*heapSort(line))

if __name__ == "__main__":
    main()



