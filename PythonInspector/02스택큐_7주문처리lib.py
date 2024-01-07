
'''
�Է�
ù ��° �ٿ� �ֹ��� ���� ��Ÿ���� ���� $n$�� �Էµ˴ϴ�. 1��n��150000
�� ��° �� ���� n�ٿ� ���� a b c�� �������� ���еǾ� �Էµ˴ϴ�.
a: ���� �湮�ϴ� �ð�
b: �ֹ��� ó���ϱ� ���� �ɸ��� �ð�
c: VIP ���� (0: �Ϲ�, 1: VIP)
(a ������ ���ĵǾ� �Է�, ������ �ð��� 2���̻��� �ֹ��� ���ٰ� ����)

���
�ֹ��� ó���Ǵ� ������ ����մϴ�. ���� ó���Ǵ� �ֹ� ��ȣ�� ���� ����ϵ��� �մϴ�.
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
#Queue�� �ڷ����ٽ� .queue[0]
#front, back ��ɾ���
#push, pop ��� put, get
#empty ��ȯ�� True flase

class orderInfo:
    '''
    �� �κ��� �������� ������.
    
    '''
    def __init__(self, t, d, v): #time duration vip
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, time, orders):
    #���׿�����: ���϶� if ������ else �������� 
    normalIndex = -1 if len(normalQueue.queue) == 0 else normalQueue.queue[0]
    vipIndex = -1 if len(vipQueue.queue) == 0 else vipQueue.queue[0]

    if vipIndex == -1:
        return normalQueue
    if normalIndex == -1:
        return vipQueue
    
    #�и� �� ���� ��� => ������
    if time < orders[normalIndex].time and  time < orders[vipIndex].time :
        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue

    #noraml�� �и����
    if time >= orders[normalIndex].time and time < orders[vipIndex].time:
        return normalQueue

    #vip�� �и����
    if time >= orders[vipIndex].time and time < orders[normalIndex].time:
        return vipQueue

    #�Ѵ� �и� ���
    return vipQueue



def processOrder(orders) :
    '''
    �ֹ� ������ �־��� ��, �ֹ��� ó���Ǵ� ������ ��ȯ�մϴ�.
    '''

    result = []
    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1 #����Ұ������� �ʱ�ȭ
    
    #Queue�� �ڷ����ٽ� .queue[0]

    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.put(i)
        else:
            vipQueue.put(i)

    #�и��ϰ�ó��
    while jobEndTime <= curTime and not (normalQueue.empty() and vipQueue.empty()):
        #normalQueue �Ǵ� vipQueue ����
        targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders)

        #ó���� �ֹ���ȣ ��������
        index = targetQueue.queue[0]

        #�ֹ�ó�� => jobEndTime����
        #jobEndTime > orders[index].time :: �з��� �ٷ� �����۾�
        #jobEndTime < orders[index].time :: �۾��� ����
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
        result.append(index + 1)
        targetQueue.get()

    #�ܾ�ó��(������ �и��ϰ�ó���� ����)
    while not (normalQueue.empty() and vipQueue.empty()):
        targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders)
        index = targetQueue.queue[0]
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
        result.append(index+1)
        targetQueue.get()      

    return result

def main():
    '''
    �� �κ��� �������� ������.
    '''

    p = int(input())

    orders = []

    for i in range(p) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))

if __name__ == "__main__":
    main()


