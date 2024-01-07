'''
입력
첫 번째 줄에 힙이 수행할 명령의 수를 나타내는 정수n을 입력합니다. (1≤n≤540000)
두 번째 줄부터 n개의 줄에 걸쳐 수행할 명령을 입력합니다. 명령의 종류는 다음과 같습니다.
0 x : 정수 x를 힙에 입력 (0≤x≤540000)
1 : 힙의 우선순위가 가장 높은 원소 제거
2 : 힙의 우선순위가 가장 높은 원소 조회

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
    우선순위 큐를 (최소)힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0] #힙의 쓰래기부분

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)
        Index = len(self.data) - 1

        while Index != 1:
            if self.data[Index//2] > self.data[Index]: # 부모값 > 자신값시 교체
                temp = self.data[Index]
                self.data[Index] = self.data[Index//2] # 부모값내리기
                self.data[Index//2] = temp # 자신값올리기
                Index = Index//2 #반복문을 위해 인덱스위치를 부모위치로 업데이트
            else: # 부모 <= 자식
                break

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        최하순위의 원소를 루트로 이동시켜 정렬을 수행합니다.
        '''
        if len(self.data) == 1: #self.data = [0]
            return -1;
        
###루트반환기능추가(lib의 일반적인 힙::팝 기능)
        root = self.data[1]
        
##마지막노드를 루트 노드 자리로 이동
        self.data[1] = self.data[-1] #(반대상황)입력시 맨마지막에 넣고 검사
        
        #힙(완전이진트리) 함수아니고, 배열 함수 : 마지막요소 제거 및 반환
        self.data.pop() # self.data[-1]

##루트로 올라온 마지막 노드를 정렬
        Index = 1
        while True:
            nextIndex = -1 #초기화

            #1-1.비교인덱스 검색 : 자식이 없는 노드
            # 총 노드 개수 < 현재 인덱스의 왼쪽자식의 노드위치 ==>종료
            if len(self.data) -1 < Index*2: 
                break

            #1-2.비교인덱스 검색 : 왼쪽 자식만 있는 경우
            # 총 노드 개수 = 현재 인덱스의 왼쪽자식의 노드위치 ==>왼쪽자식
            elif len(self.data) -1 < Index*2 +1:
                nextIndex = Index*2

            #1-3.비교인덱스 검색 : 자식이 둘인 경우
            # 총 노드 개수 > 현재 인덱스의 오른쪽자식의 노드위치 ==>자식 둘
            else:
                #현재 인덱스의 자식 노드 비교: 더 작은 쪽으로!!
                #큰 쪽을 올리면, 작은 것 위에 큰 부모가 생기됨(최소힙 위배) 
                if self.data[Index*2] < self.data[Index*2 +1]:
                    nextIndex = Index*2 #왼쪽이 작음 ==>왼쪽으로
                else: #오른쪽이 작거나 같음 ==>오른쪽으로
                    nextIndex = Index*2 +1 

            #2.현재 인덱스 vs 비교 인덱스 ==>작은 걸 위로 정렬
            if self.data[Index] > self.data[nextIndex]:
                temp = self.data[Index]
                self.data[Index] = self.data[nextIndex]
                self.data[nextIndex] = temp

                Index = nextIndex #반복을 위한 인덱스 업데이트
            else:
                break

        #lib 힙팝 스타일
        return root
                                

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 1: #self.data = [0]
            return -1
        else:
            return self.data[1]


def main():
    myPQ = PriorityQueue()

    '''
    테스트를 위한 코드입니다.
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
