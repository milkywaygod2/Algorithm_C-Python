from collections import deque
def send_message(n):
    #printNum = 2 까지는 더하고 그후론 전부 복붙 하다가 복으로 끝날것 같으면 붙한번더
    '''
    00 11 22 33 44 56 68 712
    '''
    printNum = 0
    
    if n <= 2:
        printNum += n

    if n > 2 and n % 2 == 0: #짝수
        printNum = 2 ** (n//2)
    
    if n > 2 and n % 2 == 1: #홀수
        printNum = 2 ** ((n-1)//2) + (2 ** ((n-1)//2)) // 2        
    
    return printNum

def main():
    
    while True:
        n = int(input())
        
        result = send_message(n)
    
        print(result)

if __name__ == '__main__':
    main()
