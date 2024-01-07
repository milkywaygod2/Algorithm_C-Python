'''
��, �켱���� ť�� �̿��Ͽ� �����ϵ��� �մϴ�.

�Է°�
ù ��° �ٿ� n���� ���ڰ� �������� ���еǾ� �־����ϴ�.
10 9 8 7 6 5 4 3 2 1

1 2 3 4 5 6 7 8 9 10
'''
'''
heapSort �Լ��� �����ϼ���.
'''
import heapq                                #lib
class PriorityQueue:
    '''
    �켱���� ť�� (�ּ�)������ �����մϴ�
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
    items�� �ִ� ���Ҹ� heap sort�Ͽ� ����Ʈ�� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.

    ��, ������ �ۼ��Ͽ��� priorityQueue�� �̿��ϼ���.
    '''

    result = []
    pq = PriorityQueue() #�ּ���
    for item in items:
        pq.push(item)
    
    for i in range(len(items)):
        result.append(pq.top())
        pq.pop() #�ǵڿ��� ������ �ø��� ���ı���

    return result

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    print(*heapSort(line))

if __name__ == "__main__":
    main()



