
'''
�Է�
ù ��° �ٿ� ����� ������ ��Ÿ���� ���� n�� �Էµ˴ϴ�. (1��n��1000)
�� ��° �ٺ��� n�ٿ� ���� ���� a b c�� �������� ���еǾ� �Էµ˴ϴ�.
���� a�� ���� �ڽ����� b, ������ �ڽ����� c�� ���´ٴ� �ǹ��Դϴ�. ���� ����� �ڽ� ��尡 ���ٸ� -1�� �־����ϴ�.
��, ù ��°�� �־����� ������ ������ ��Ʈ ��尡 �ԷµǸ� ��Ʈ ��尡 ���� ���� 1�Դϴ�.
�̿��� �� �������� �̹� �Էµ� ������ �� �ϳ��� �θ� ���� ���� ��츸 �Էµ˴ϴ�.
�� ������ ���׹��� �ԷµǴ� ���� �����ϴ�.

���
Tree Ŭ������ �ùٸ��� �ۼ��ؾ� �մϴ�.
Tree Ŭ������ ������ �ùٸ��� Ȯ���ϱ� ���Ͽ� preorder, inorder, postorder �Լ��κ��� ���� ����, ����, ���� ��ȸ�� ����� ��µ˴ϴ�.

5
1 2 3
2 4 5
3 -1 -1
4 -1 -1
5 -1 -1

1 2 4 5 3
4 2 5 1 3
4 5 2 3 1

��ó�� �������� Ʈ���Է��� �� ������
1 2 3
4 5 6
7 8 9
�� ���� ���������� �Է��� �������� Ʈ����ä�� ����� ������ ����.
'''


class Tree:
    #� Ʈ���� ��Ʈ ��带 �����ִ�
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    #����� Ư��
    # : �ڽ� if ���� ����� �ڽ�? else �ڽ��߿� ��� �� �ڽ�����
    def addNode(self, i, l, r) :
        '''
        Ʈ�� ���� ���� i�� ���Ͽ� �����ڽ��� l, ������ �ڽ��� r��
        �������ִ� �Լ��� �ۼ��ϼ���.
        '''
        #��Ʈ��� Ȥ�� i����ڽſ��� �ڽĺο�
        #����addNode������ self.index�� vs ���ο� i
        if self.index == None or self.index == i:  
      
            self.index = i #���ο� i�� self.index������Ʈ

            #���ʰ�ü
            self.left = Tree(l,None,None) if l != None else None 

            #�����ʰ�ü
            self.right = Tree(r,None,None) if r != None else None

            return True

        #�ڽ��� �ڽĿ��� �ڽĺο���Ȳ
        else:
            #flag�� ���� �� ������ Ž��
            flag = False

            #�����ڽ��ִٸ�
            if self.left != None: 
                flag = self.left.addNode(i,l,r) #���ʰ�ü�� addNode

            #���ʽ��� �����ڽ��ִٸ�
            if flag == False and self.right != None: 
                flag = self.right.addNode(i,l,r)

            return flag

from tree import Tree
from treeTraversal import preorder, inorder, postorder

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
