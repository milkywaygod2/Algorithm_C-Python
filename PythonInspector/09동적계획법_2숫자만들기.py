'''
���� �����
1���� 3������ ���� ���Ͽ� 5�� ����� ����� ���� ������ ���� 13������ �����մϴ�.
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 2 + 1
1 + 2 + 1 + 1
2 + 1 + 1 + 1
1 + 2 + 2
2 + 1 + 2
2 + 2 + 1
1 + 1 + 3
1 + 3 + 1
3 + 1 + 1
2 + 3
3 + 2
1���� m������ ���� ���Ͽ� n�� ����� ����� ���� ���ϴ� ���α׷��� �ۼ��ϼ���. 
��, ����� ���� �ſ� Ŀ�� �� �����Ƿ�, ����� ���� 1,000,000,007 �� ���� �������� ����մϴ�.
5 3

13

1 ~ m ������ ���� ���Ͽ� n�� ����� ����� ���� 1,000,000,007�� ���� �������� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���. ��, ����� ���� �ſ� Ŀ�� �� �����Ƿ�, ����� ���� 1,000,000,007 �� ���� �������� ����մϴ�.
    sum1to3(5) 
    = sum1to3(5-1)+sum1to3(5-2)+sum1to3(5-3)+sum1to3(5-4)+sum1to3(5-5)
    = sum1to3(4)+sum1to3(3)+sum1to3(2)+sum1to3(1)+sum1to3(0)    
    = {sum1to3(4-1)+sum1to3(3-1)+sum1to3(2-1)+sum1to3(1-1)}   // sum1to3(4)
                  +{sum1to3(3-1)+sum1to3(2-1)+sum1to3(1-1)}   // sum1to3(3)
                               +{sum1to3(2-1)+sum1to3(1-1)}   // sum1to3(2)
                                             +sum1to3(1-1)    // sum1to3(1)
                                             +1����           // sum1to3(0)
    =...�߷�
    
'''
def makeNumber(n, m) : #_for���Ҿ�, �ݺ���
    #��ȭ�� result[n] = �ñ׸�(i=1~m)::result[n-i]

    resultArr4_eachCases = [1] #n=0 ����

    #����ȭ���� N-1 + N-2 + ..������ ��N������ �� ���� ���� ������ ������ �Ǿ����� 
    #N-1 = (N-1)-1 + (N-1)-2.. 
    #N-2 = (N-2)-1 + (N-2)-2..
    #�ᱹ 1~n �� ��ȭ�Ŀ� ���� n��ŭ �ݺ���
    for N in range(1,n+1): 

        #�Ʒ��� ���� ��ȭ�� �κ�
        sumDP_recursion = 0
        for i in range(1, min(N,m)+1): #1~m, ���� �� N���ٴ� i�� �۰ų� ���ƾ���,n-m���� m�� ��ũ�� ������ �Ǵϱ�
            sumDP_recursion += resultArr4_eachCases[N-i]
        resultArr4_eachCases.append(sumDP_recursion%1000000007) #n ĳ�̽����� �迭�� ����
    return resultArr4_eachCases[n]


def makeNumber_recur(n, m) : #_recurž�ٿ�, ��ͽ�

    resultArr4_eachCases = [1] #n=0 ����

    if not n in resultArr4_eachCases:
        #�Ʒ��� ���� ��ȭ�� �κ�
        sumDP_recursion = 0
        for i in range(1, min(n,m)+1): #1~m, ���� �� N���ٴ� i�� �۰ų� ���ƾ���
            sumDP_recursion += makeNumber_recur(n-i, m)
        resultArr4_eachCases[n] = sumDP_recursion%1000000007 #[n] ĳ�̽��� ���� ��ͽ����� ������ ������ [0]���� ���Ե�
    return resultArr4_eachCases[n]


def main():
    '''
    �Ʒ� �κ��� �������� ������.
    '''

    firstLine = [int(x) for x in input().split()]

    n = firstLine[0]
    m = firstLine[1]

    print(makeNumber(n, m))

if __name__ == "__main__":
    main()
