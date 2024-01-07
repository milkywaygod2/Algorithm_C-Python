'''
1.��ǥ: maxSum(n) = n��° ���ڷ� ������(�����ʳ�) ���Ӻκ��ִ���
2.�κй�����ȭ��: 
�ΰ������
maxSum(n-1)�� ����n��° ���� �����ϱ� (������ �ϳ���) //maxSum(n-1) + arr(n)
n��°���� ���Ӱ� �������� �����ϱ� (���ο� ����) //0 + arr(n)
maxSum(n) = max(maxSum(n-1),0) + arr(n)

���Ӻκ��ִ���
1 2 -4 5 3 -2 9 -10
15
'''

def getSubsum(data) :
    '''
    n���� ���ڰ� list�� �־��� ��, 
    �� ���� �κ� �ִ����� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    '''
    maxSum = []
    final_max = data[0]
    maxSum.append(data[0])

    for n in range(1,len(data)):
        maxSum.append(max(maxSum[n-1],0) + data[n])
        if final_max < maxSum[n]:
            final_max = maxSum[n]    
    
    return final_max

def getSubsum_recur(data): #???
    n = len(data)
    maxSum = [None]*n
    final_max = data[0]
    maxSum.append(data[0])

    if maxSum[n] is not None:
        return maxSum[n]
    else:
        maxSum.append(max(maxSum[n-1],0) + data[n])



import sys

def main():
    '''
    �� �κ��� �������� ������.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
