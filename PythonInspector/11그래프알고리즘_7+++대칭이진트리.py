'''
��Ī ����Ʈ��
�־��� ����Ʈ���� �¿� ��Ī���� �Ǵ��ϴ� ���α׷��� �ۼ��Ͻÿ�. ���� ���, ������ Ʈ���� ��Ī�̴�.

�Է�
ù ��° �ٿ� ����� ���� n�� �־�����. �� ��° �ٿ� n���� ���ڰ� �־�����, �̴� �� ����� ���� ��Ÿ����. 
�� ��° �ٺ��� n���� �ٿ� ���Ͽ� ������ ������ �־�����. �� ���� �� ���� ���� a, b, c�� �̷�� ����, 
�̴� ���� a�� ���� �ڽ����� b, ������ �ڽ����� c�� ���´ٴ� �ǹ��̴�. ���� ���� �ڽĳ�尡 ���ٸ� -1�� �־�����.

���
�־��� ����Ʈ���� �¿� ��Ī�̸� Yes, �ƴϸ� No�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է� ���� 1
7
1 2 4 3 2 3 4
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 6
5 -1 -1
6 -1 -1

��� ���� 1
Yes

�Է� ���� 2
5
1 2 2 3 3
0 1 2
1 3 -1
2 4 -1
3 -1 -1
4 -1 -1

��� ���� 2
No
'''
def symmetricTree(tree, nodeValue):
    '''
    �־��� tree�� �¿� ��Ī�̸� True, �ƴϸ� False�� ��ȯ�ϴ� �Լ�.

    ��, nodeValue[i] : Node i�� ���� ��Ÿ����, 
        tree[i][0] : Node i�� ���� Node�� index,
        tree[i][1] : Node i�� ������ Node�� index�� ��Ÿ����.
        ��, �ڽ� Node�� �������� ���� ��� index�� -1�̴�.

    '''

    result = True

    return result

#main.py
from symmetricTree import symmetricTree

def main():
    '''
    Do not change this code
    '''
    
    n = int(input())
    nodeValue = [int(x) for x in input().split()]
    tree = [ [] for x in range(n) ]

    for i in range(n) :
        line = [int(x) for x in input().split()]
        tree[line[0]].append(line[1])
        tree[line[0]].append(line[2])

    if(symmetricTree(tree, nodeValue) == True) :
        print("Yes")
    else :
        print("No")

if __name__ == "__main__":
    main()
