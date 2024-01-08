'''
n : 엘리스가 전송해야 할 암호 문자의 개수
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
    #printNum = 2 까지는 더하고 그후론 전부 복붙 하다가 복으로 끝날것 같으면 붙 한번더
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




from collections import deque
def send_message_queue(n):
    check = [ [0 for _ in range(1001)] for _ in range(1001)]  #0라인은 실상 안씀?
    queue = deque()
    queue.append([0, 0, 0]) #화면문자수, 버퍼, 시간

    while queue: #완전히 빌때까지
        printNum, clipboard, time = queue.popleft() #변수로 저장
        
        #목표달성?
        if time == n: 
            return printNum

        #재방문?
        if check[printNum][clipboard]:
            continue #Yes
        else: #No 최초방문
            check[printNum][clipboard] = 1 #방문표시
            
            queue.append([printNum+1, clipboard, time+1])               #추가경우

            if printNum: #뭔가있으면                                          
                queue.append([printNum, printNum, time+1])              #복사경우

            if clipboard: #뭔가있으면                                    
                queue.append([printNum+clipboard, clipboard, time+1])   #붙여넣기
                
def main():
    '''
    테스트를 위한 코드입니다.
    '''
    
    n = int(input())
        
    result = send_message(n)
    
    print(result)

if __name__ == '__main__':
    main()
