
'''
입력
첫 번째 줄에 노드의 개수를 의미하는 n이 입력됩니다.
두 번째 줄 부터 n개의 줄에 걸쳐 노드들의 관계가 세 개의 정수로 구분되어 주어집니다.(n≤1000)
x y z꼴의 입력은, x번 노드의 왼쪽 자식이 y, 오른쪽 자식이 z라는 의미입니다.

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
    getHeight 함수를 작성하세요.
    모든 리프노드의 깊이를 구한 후 가장 깊은 깊이에 +1
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right)) #재귀!!

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
