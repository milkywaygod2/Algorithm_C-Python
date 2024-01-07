'''
josephus_sequence �Լ��� �ۼ��ϼ���.

�Է�
ù ��° �ٿ� ���� N�� K�� ������ �������� �Էµ˴ϴ�.(1��K��N��1000)

7 3

3 6 2 7 5 1 4
'''
from queue import Queue

#n���� ����� k��° ���� �ԾƳ�
def josephus_sequence(n, k) :
    # ���n���� ť�� ��ġ
    q = Queue()

    result = []
    for i in range(1,n+1): #1���ͽ���
        q.put(i)

    while not q.empty():
        for i in range(k): #0���ͽ���
            num = q.get()
            if i == k-1:
                result.append(num)
            else:
                q.put(num)

    return result

def main():
    '''
    �� �κ��� �������� ������.
    '''

    n, k = [int(v) for v in input().split()]

    print(josephus_sequence(n, k))

if __name__ == "__main__":
    main()


