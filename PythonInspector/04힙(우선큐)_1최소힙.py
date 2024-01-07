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

1
2
'''
class PriorityQueue:
    '''
    �켱���� ť�� (�ּ�)������ �����մϴ�
    '''

    def __init__(self) :
        self.data = [0] #���� ������κ�

    def push(self, value) :
        '''
        �켱���� ť�� value�� �����մϴ�.
        '''
        self.data.append(value)
        Index = len(self.data) - 1

        while Index != 1:
            if self.data[Index//2] > self.data[Index]: # �θ� > �ڽŰ��� ��ü
                temp = self.data[Index]
                self.data[Index] = self.data[Index//2] # �θ𰪳�����
                self.data[Index//2] = temp # �ڽŰ��ø���
                Index = Index//2 #�ݺ����� ���� �ε�����ġ�� �θ���ġ�� ������Ʈ
            else: # �θ� <= �ڽ�
                break

    def pop(self) :
        '''
        �켱������ ���� ���� ���Ҹ� �����մϴ�.
        ���ϼ����� ���Ҹ� ��Ʈ�� �̵����� ������ �����մϴ�.
        '''
        if len(self.data) == 1: #self.data = [0]
            return -1;
        
###��Ʈ��ȯ����߰�(lib�� �Ϲ����� ��::�� ���)
        root = self.data[1]
        
##��������带 ��Ʈ ��� �ڸ��� �̵�
        self.data[1] = self.data[-1] #(�ݴ��Ȳ)�Է½� �Ǹ������� �ְ� �˻�
        
        #��(��������Ʈ��) �Լ��ƴϰ�, �迭 �Լ� : ��������� ���� �� ��ȯ
        self.data.pop() # self.data[-1]

##��Ʈ�� �ö�� ������ ��带 ����
        Index = 1
        while True:
            nextIndex = -1 #�ʱ�ȭ

            #1-1.���ε��� �˻� : �ڽ��� ���� ���
            # �� ��� ���� < ���� �ε����� �����ڽ��� �����ġ ==>����
            if len(self.data) -1 < Index*2: 
                break

            #1-2.���ε��� �˻� : ���� �ڽĸ� �ִ� ���
            # �� ��� ���� = ���� �ε����� �����ڽ��� �����ġ ==>�����ڽ�
            elif len(self.data) -1 < Index*2 +1:
                nextIndex = Index*2

            #1-3.���ε��� �˻� : �ڽ��� ���� ���
            # �� ��� ���� > ���� �ε����� �������ڽ��� �����ġ ==>�ڽ� ��
            else:
                #���� �ε����� �ڽ� ��� ��: �� ���� ������!!
                #ū ���� �ø���, ���� �� ���� ū �θ� �����(�ּ��� ����) 
                if self.data[Index*2] < self.data[Index*2 +1]:
                    nextIndex = Index*2 #������ ���� ==>��������
                else: #�������� �۰ų� ���� ==>����������
                    nextIndex = Index*2 +1 

            #2.���� �ε��� vs �� �ε��� ==>���� �� ���� ����
            if self.data[Index] > self.data[nextIndex]:
                temp = self.data[Index]
                self.data[Index] = self.data[nextIndex]
                self.data[nextIndex] = temp

                Index = nextIndex #�ݺ��� ���� �ε��� ������Ʈ
            else:
                break

        #lib ���� ��Ÿ��
        return root
                                

    def top(self) :
        '''
        �켱������ ���� ���� ���Ҹ� ��ȯ�մϴ�. ���� �켱���� ť�� ����ִٸ� -1�� ��ȯ�մϴ�.
        '''
        if len(self.data) == 1: #self.data = [0]
            return -1
        else:
            return self.data[1]


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
