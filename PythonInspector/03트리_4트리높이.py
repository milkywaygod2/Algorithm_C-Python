
'''
�Է�
ù ��° �ٿ� ����� ������ �ǹ��ϴ� n�� �Էµ˴ϴ�.
�� ��° �� ���� n���� �ٿ� ���� ������ ���谡 �� ���� ������ ���еǾ� �־����ϴ�.(n��1000)
x y z���� �Է���, x�� ����� ���� �ڽ��� y, ������ �ڽ��� z��� �ǹ��Դϴ�.

5
1 2 3
2 4 5
3 -1 -1
4 -1 -1
5 -1 -1

3
'''

def getHeight(myTree) :
    '''
    getHeight �Լ��� �ۼ��ϼ���.
    ��� ��������� ���̸� ���� �� ���� ���� ���̿� +1
    myTree�� ���̸� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    '''
    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right)) #���!!

    return 0


from tree import Tree
def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n) :
        myList = [int(v) for v in input().split()]

        if myList[1] == -1 :
            myList[1] = None

        if myList[2] == -1 :
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(getHeight(myTree))


if __name__ == "__main__":
    main()
