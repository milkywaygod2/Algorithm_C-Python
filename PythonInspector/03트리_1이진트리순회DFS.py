
'''
�Է�
ù ��° �ٿ� ����� ������ ��Ÿ���� ���� n�� �Էµ˴ϴ�. (1��n��1000)
�� ��° �ٺ��� n�ٿ� ���� ���� a b c�� �������� ���еǾ� �Էµ˴ϴ�.
���� a�� ���� �ڽ����� b, ������ �ڽ����� c�� ���´ٴ� �ǹ��Դϴ�. ���� ����� �ڽ� ��尡 ���ٸ� -1�� �־����ϴ�.
��, ù ��°�� �־����� ������ ������ ��Ʈ ��尡 �ԷµǸ� ��Ʈ ��尡 ���� ���� 1�Դϴ�.
�̿��� �� �������� �̹� �Էµ� ������ �� �ϳ��� �θ� ���� ���� ��츸 �Էµ˴ϴ�.
�� ������ ���׹��� �ԷµǴ� ���� �����ϴ�.
5
1 2 3
2 4 5
3 -1 -1
4 -1 -1
5 -1 -1

1 2 4 5 3
4 2 5 1 3
4 5 2 3 1
'''

def preorder(tree) :
    '''
    preorder, inorder, postorder �Լ��� �����ϼ���.
    tree�� ������ȸ �Ͽ� ����Ʈ�� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    '''
    
    result = []
    
    #1��Ʈ���
    result.append(tree.index)

    #2���� ����Ʈ����ȸ
    if tree.left != None:
        result = result + preorder(tree.left)

    #3������ ����Ʈ����ȸ
    if tree.right != None:
        result = result + preorder(tree.right)

    return result

def inorder(tree) :
    '''
    tree�� ������ȸ �Ͽ� ����Ʈ�� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    '''
    result = []

    #1���� ����Ʈ����ȸ
    if tree.left != None:
        result = result + inorder(tree.left)

    #2��Ʈ���
    result.append(tree.index)

    #3������ ����Ʈ����ȸ
    if tree.right != None:
        result = result + inorder(tree.right)

    return result

def postorder(tree) :
    '''
    tree�� ������ȸ �Ͽ� ����Ʈ�� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    '''
    result = []

    #1���� ����Ʈ����ȸ
    if tree.left != None:
        result = result + postorder(tree.left)

    #2������ ����Ʈ����ȸ
    if tree.right != None:
        result = result + postorder(tree.right)
        
    #3��Ʈ���
    result.append(tree.index)


    return result



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

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))


if __name__ == "__main__":
    main()
