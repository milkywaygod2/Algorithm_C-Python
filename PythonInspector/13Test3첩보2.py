'''
n : �������� �����ؾ� �� ��ȣ ������ ����
bfs
'''
def send_message(n) :
    d = [ 0 for i in range(10001) ]
 
    d[1] = 1
    d[2] = 2
 
    for i in range(3, 101):
        for j in range(1, i-1):
            d[i] = max(d[i], d[i-1]+1, d[i-(1+j)]*(1+j))
    return d[n]

def send_message_my(n):
    #printNum = 2 ������ ���ϰ� ���ķ� ���� ���� �ϴٰ� ������ ������ ������ �� �ѹ���
    '''
    00 11 22 33 44 56 68 712
    '''
    printNum = 0
    
    if n <= 2:
        printNum += n

    if n > 2 and n % 2 == 0: #¦��
        printNum = 2 ** (n//2)
    
    if n > 2 and n % 2 == 1: #Ȧ��
        printNum = 2 ** ((n-1)//2) + (2 ** ((n-1)//2)) // 2        
    
    return printNum




from collections import deque
def send_message_queue(n):
    check = [ [0 for _ in range(1001)] for _ in range(1001)]  #0������ �ǻ� �Ⱦ�?
    queue = deque()
    queue.append([0, 0, 0]) #ȭ�鹮�ڼ�, ����, �ð�

    while queue: #������ ��������
        printNum, clipboard, time = queue.popleft() #������ ����
        
        #��ǥ�޼�?
        if time == n: 
            return printNum

        #��湮?
        if check[printNum][clipboard]:
            continue #Yes
        else: #No ���ʹ湮
            check[printNum][clipboard] = 1 #�湮ǥ��
            
            queue.append([printNum+1, clipboard, time+1])               #�߰����

            if printNum: #����������                                          
                queue.append([printNum, printNum, time+1])              #������

            if clipboard: #����������                                    
                queue.append([printNum+clipboard, clipboard, time+1])   #�ٿ��ֱ�
                
def main():
    '''
    �׽�Ʈ�� ���� �ڵ��Դϴ�.
    '''
    
    n = int(input())
        
    result = send_message(n)
    
    print(result)

if __name__ == '__main__':
    main()
