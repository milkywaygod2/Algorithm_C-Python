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

1 2 3 4 5
'''
from queue import Queue
def BFS(tree) :
    '''
    tree�� �ʺ� �켱 Ž������ ��ȸ�Ͽ� ����Ʈ�� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    '''
    q = Queue()

    #��Ʈ
    q.put(tree)
    
    result = []

    #q�� ���� �ִٸ� ��� �ݺ�
    while len(q.queue) > 0:
        cur = q.get()
        if cur == None :
            continue
        result.append(cur.index)
        q.put(cur.left)
        q.put(cur.right)

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

    print(*BFS(myTree))


if __name__ == "__main__":
    main()

