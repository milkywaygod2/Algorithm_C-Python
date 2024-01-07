
'''
입력
첫 번째 줄에 주문의 수를 나타내는 정수 $n$이 입력됩니다. 1≤n≤150000
두 번째 줄 부터 n줄에 걸쳐 a b c가 공백으로 구분되어 입력됩니다.
a: 고객이 방문하는 시간
b: 주문을 처리하기 위해 걸리는 시간
c: VIP 여부 (0: 일반, 1: VIP)
(a 순으로 정렬되어 입력, 동일한 시간에 2개이상의 주문은 없다고 가정)

결과
주문이 처리되는 순서를 출력합니다. 먼저 처리되는 주문 번호를 먼저 출력하도록 합니다.
4
1 3 0
4 3 0
7 3 0
10 3 0

1 2 3 4

4
1 3 0
3 3 0
5 3 0
7 3 1

1 2 4 3

9
1 4 0
3 1 0
4 1 0
5 4 1
6 5 0
7 4 0
9 4 1
13 4 1
17 4 1

1 4 7 8 9 2 3 5 6
'''
from queue import Queue
#Queue의 자료접근시 .queue[0]
#front, back 기능없음
#push, pop 대신 put, get
#empty 반환은 True flase

class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    
    '''
    def __init__(self, t, d, v): #time duration vip
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, time, orders):
    #삼항연산자: 참일때 if 참조건 else 거짓조건 
    normalIndex = -1 if len(normalQueue.queue) == 0 else normalQueue.queue[0]
    vipIndex = -1 if len(vipQueue.queue) == 0 else vipQueue.queue[0]

    if vipIndex == -1:
        return normalQueue
    if normalIndex == -1:
        return vipQueue
    
    #밀린 게 없는 경우 => 선착순
    if time < orders[normalIndex].time and  time < orders[vipIndex].time :
        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue

    #noraml만 밀린경우
    if time >= orders[normalIndex].time and time < orders[vipIndex].time:
        return normalQueue

    #vip만 밀린경우
    if time >= orders[vipIndex].time and time < orders[normalIndex].time:
        return vipQueue

    #둘다 밀린 경우
    return vipQueue



def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''

    result = []
    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1 #존재불가값으로 초기화
    
    #Queue의 자료접근시 .queue[0]

    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.put(i)
        else:
            vipQueue.put(i)

    #밀린일감처리
    while jobEndTime <= curTime and not (normalQueue.empty() and vipQueue.empty()):
        #normalQueue 또는 vipQueue 선택
        targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders)

        #처리할 주문번호 가져오기
        index = targetQueue.queue[0]

        #주문처리 => jobEndTime증가
        #jobEndTime > orders[index].time :: 밀려서 바로 다음작업
        #jobEndTime < orders[index].time :: 작업간 여유
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
        result.append(index + 1)
        targetQueue.get()

    #잔업처리(본문은 밀린일감처리와 동일)
    while not (normalQueue.empty() and vipQueue.empty()):
        targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders)
        index = targetQueue.queue[0]
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
        result.append(index+1)
        targetQueue.get()      

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    p = int(input())

    orders = []

    for i in range(p) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))

if __name__ == "__main__":
    main()


