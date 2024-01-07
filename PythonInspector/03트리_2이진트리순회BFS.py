'''
입력
첫 번째 줄에 노드의 개수를 나타내는 정수 n이 입력됩니다. (1≤n≤1000)
두 번째 줄부터 n줄에 걸쳐 정수 a b c가 공백으로 구분되어 입력됩니다.
정점 a가 왼쪽 자식으로 b, 오른쪽 자식으로 c를 갖는다는 의미입니다. 만약 노드의 자식 노드가 없다면 -1이 주어집니다.
단, 첫 번째로 주어지는 정점은 무조건 루트 노드가 입력되며 루트 노드가 갖는 값은 1입니다.
이외의 각 정점들은 이미 입력된 정점들 중 하나를 부모 노드로 갖는 경우만 입력됩니다.
즉 정점이 뒤죽박죽 입력되는 경우는 없습니다.
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
    tree를 너비 우선 탐색으로 순회하여 리스트로 반환하는 함수를 작성하세요.
    '''
    q = Queue()

    #루트
    q.put(tree)
    
    result = []

    #q에 뭔가 있다면 계속 반복
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

