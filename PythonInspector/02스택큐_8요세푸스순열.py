'''
josephus_sequence 함수를 작성하세요.

입력
첫 번째 줄에 정수 N과 K가 공백을 기준으로 입력됩니다.(1≤K≤N≤1000)

7 3

3 6 2 7 5 1 4
'''
from queue import Queue

#n명의 사람을 k번째 마다 솎아냄
def josephus_sequence(n, k) :
    # 사람n명을 큐에 배치
    q = Queue()

    result = []
    for i in range(1,n+1): #1부터시작
        q.put(i)

    while not q.empty():
        for i in range(k): #0부터시작
            num = q.get()
            if i == k-1:
                result.append(num)
            else:
                q.put(num)

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n, k = [int(v) for v in input().split()]

    print(josephus_sequence(n, k))

if __name__ == "__main__":
    main()


