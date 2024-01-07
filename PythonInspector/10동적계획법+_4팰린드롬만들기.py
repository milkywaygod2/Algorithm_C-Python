#�縰���: �Ųٷ� �ص� '������'
'''
���ڿ� data�� �־��� ��, �̸� �Ӹ�������� ����� ���� �����ؾ� �ϴ� ���� ������ �ּڰ��� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
abcfba

1
'''
#��ȭ�� 
# if (data[i] == data[j]) then p[i][j] = p[i+1][j-1] 
# if (data[i] != data[j]) then p[i][j] = min(p[i+1][j], p[i][j-1]) + 1 
def palindrome(data) :
    n = len(data)
    p = [[0]*n for i in range(n)] #�ʱ�ȭ�� ��������

    #�����ʳ��ι�°���� �ٷο����ʺ��� �����ʳ����� Ž��, ������ ���ʳ����� �ݺ��ϸ� ����Ž��
    #�����ʳ����� ������ Ž���ϱ⶧���� Ȯ��� ������ ���ؼ� else�� ���� �迭�� ����� ���� ����
    for i in range(n-2, -1, -1): #n-2(������ �ι�°)���� -1����(0)����
        for j in range(i+1, n): #i+1 ������ �������� ��(n)����
            if data[i] == data[j]:
                p[i][j] = p[i+1][j-1]
            else:
                p[i][j] = min(p[i+1][j], p[i][j-1]) + 1 #���鼭 p�迭�� �Ӹ���Ұ� ����
    return p[0][len(data)-1]

import sys
def main():
    '''
    �� �κ��� �������� ������.
    '''

    s = input()

    print(palindrome(s))

if __name__ == "__main__":
    main()
