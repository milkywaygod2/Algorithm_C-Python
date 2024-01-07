
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

2 4
'''
def inorder(tree, depth):
    result=[]
    
    if tree.left != None:
        result += inorder(tree.left, depth + 1)

    tree.setDepth(depth)
    result.append(tree) #���Ϳ� �����ϴ� ���� ��ü�� ��� ������ ��.

    if tree.right != None:
        result += inorder(tree.right, depth + 1)

    return result

def getWidth(myTree) :
    '''
    myTree�� �ʺ� ���� ���� ������ �� ������ �ʺ� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    ���� ���� ���� l�� �� ������ �ʺ� w�� Ʃ�÷� ��ȯ�ؾ� �մϴ�.
    
    ��ȯ�� ���� : (l, w)
    '''
##Ʈ������_��Ʈ
    result = inorder(myTree, 1) #�迭result�� ����1���ͽ���

##Ʈ����������Ϳ�_��������
    n = len(result)

    #���̴� �ִ� 1000���� => �ִ���� 1001 => �ε����� 0~1001
    left =[1001 for i in range(1001)] # 0~1000�ε����� ���Ҵ� ���� 1001(�Ұ����ʱⰪ, �����ʺ��� �������� �Ĳ��� �˻�)
    right = [-1 for i in range(1001)] # 0~1000�ε����� ���Ҵ� ���� -1(�Ұ����ʱⰪ, ���ʺ��� ���������� �Ĳ��� �˻�)
    maxDepth = 0

##Ʈ�����������������_����
    for i in range(n):      #i �˻����� ���� ����� ��ġ
        d = result[i].depth #d ������ȸ�������� ���� ���(i)�� ���� (�ִ����1000����)

        #�ᱹ ���� ���� d�� i�鳢�� i vs i �� ��� ���Ͽ� �������� �� �迭�� ���� ���� d �ε����� ����
        left[d] = min(left[d], i) #�迭left�� �ε���d�� i�� ����, min(1001,i)���� �����ؼ� ���: ����� 1001�� �ε���=>��������X
        right[d] = max(right[d], i) #�迭right�� �ε���d�� i�� ����, max(-1,i)���� �����ؼ� ���: ����� -1�� �ε���=>��������X
        maxDepth = max(maxDepth, d) #�ִ���̴� ���� ��� max(0,d)�� ���� ���

##Ʈ��������_����
    widestDepth = 0
    widestLength = 0
    for d in range(1, maxDepth+1): #����d�� ���ؼ� for��, ��Ʈ �ڽ��� ����

        width = right[d] - left[d] + 1 # �ʺ����:����, ����1�� ��Ʈ������ right[1] = left[1]
        if widestLength < width:
            widestLength = width
            widestDepth = d #������
 
    return (widestDepth, widestLength)

    return (0, 0)

class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r
        self.depth = -1

    def setDepth(self, d) :
        self.depth = d

    def addNode(self, i, l, r) :
        if self.index == None or self.index == i :
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None
            return True

        else :
            flag = False

            if self.left != None :
                flag = self.left.addNode(i, l, r)

            if flag == False and self.right != None :
                flag = self.right.addNode(i, l, r)

            return flag