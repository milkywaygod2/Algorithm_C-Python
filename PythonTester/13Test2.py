from collections import deque
def send_message(n):
    #printNum = 2 ������ ���ϰ� ���ķ� ���� ���� �ϴٰ� ������ ������ ������ ���ѹ���
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

def main():
    
    while True:
        n = int(input())
        
        result = send_message(n)
    
        print(result)

if __name__ == '__main__':
    main()
