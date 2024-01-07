'''
�Է�
ù ��° �ٿ� ���� ������ ����� ���� ��Ÿ���� ����n�� �Է��մϴ�. (1��n��540000)
�� ��° �ٺ��� n���� �ٿ� ���� ������ ����� �Է��մϴ�. ����� ������ ������ �����ϴ�.
0 x : ���� x�� ���� �Է� (0��x��540000)
1 : ���� �켱������ ���� ���� ���� ����
2 : ���� �켱������ ���� ���� ���� ��ȸ

8
0 1
0 4
0 3
0 2
2
1
2
1

4
3
'''
import heapq #lib

class PriorityQueue:
    '''
    �켱���� ť�� (�ּ�)������ �����մϴ�
    '''

    def __init__(self) :
        self.data = [] 

    def push(self, value) :
         heapq.heappush(self.data, -value) #������ȯ

    def pop(self) :
        if len(self.data) > 0:
            heapq.heappop(self.data) 

    def top(self) :
        if len(self.data) == 0: 
            return -1           
        else:                   
            return -self.data[0] #����


def main():
    myPQ = PriorityQueue()

    '''
    �׽�Ʈ�� ���� �ڵ��Դϴ�.
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
