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

class Queue:
    '''
    List�� �̿��Ͽ� ������ method���� �ۼ��ϼ���.
    '''
    def __init__(self) :
        '''
        ť myQueue�� ����ϴ�.
        '''
        self.myQueue = []
        pass

    def push(self, n) :
        '''
        queue�� ���� n�� �ֽ��ϴ�.
        '''
        self.myQueue.append(n)
        pass

    def pop(self) :
        '''
        queue���� ���� �տ� �ִ� ������ �����մϴ�. 
        ���� queue�� ����ִ� ���� ���� ��쿡�� �ƹ� �ϵ� ���� �ʽ��ϴ�. 
        '''
        if self.empty() == 1:
            return
        else:
            del self.myQueue[0]
        pass

    def size(self) :
        '''
        queue�� ��� �ִ� ������ ������ return �մϴ�.
        '''
        return len(self.myQueue)
        pass

    def empty(self) :
        '''
        queue�� ����ִٸ� 1, �ƴϸ� 0�� return �մϴ�.
        '''
        if self.size() == 0:
            return 1
        else:
            return 0
        pass

    def front(self) :
        '''
        queue�� ���� �տ� �ִ� ������ return �մϴ�. 
        ���� queue�� ����ִ� ���� ���� ��쿡�� -1�� return �մϴ�.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[0]
        pass

    def back(self) :
        '''
        queue�� ���� �ڿ� �ִ� ������ return �մϴ�. 
        ���� queue�� ����ִ� ���� ���� ��쿡�� -1�� return �մϴ�.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[-1]
        pass
        
################
class orderInfo:
    '''
    �� �κ��� �������� ������.
    '''
    def __init__(self, t, d, v): #time duration vip
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue,vipQueue,time, orders):
    normalIndex = normalQueue.front()
    vipIndex = vipQueue.front()

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
    
    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.push(i)
        else:
            vipQueue.push(i)

    #�и��ϰ�ó��
    while jobEndTime <= curTime and not (normalQueue.empty() == 1 and vipQueue.empty() == 1):
        #normalQueue �Ǵ� vipQueue ����
        targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders)

        #ó���� �ֹ���ȣ ��������
        index = targetQueue.front()

        #�ֹ�ó�� => jobEndTime����
        #jobEndTime > orders[index].time :: �з��� �ٷ� �����۾�
        #jobEndTime < orders[index].time :: �۾��� ����
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
        result.append(index + 1)
        targetQueue.pop()

    #�ܾ�ó��(������ �и��ϰ�ó���� ����)
    while not (normalQueue.empty() == 1 and vipQueue.empty() == 1):
        targetQueue = selectQueue(normalQueue,vipQueue,jobEndTime,orders)
        index = targetQueue.front()
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
        result.append(index+1)
        targetQueue.pop()      

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


