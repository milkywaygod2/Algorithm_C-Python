
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

1 2 4 5 3
4 2 5 1 3
4 5 2 3 1
'''

def preorder(tree) :
    '''
    preorder, inorder, postorder 함수를 구현하세요.
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    
    result = []
    
    #1루트노드
    result.append(tree.index)

    #2왼쪽 서브트리순회
    if tree.left != None:
        result = result + preorder(tree.left)

    #3오른쪽 서브트리순회
    if tree.right != None:
        result = result + preorder(tree.right)

    return result

def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    #1왼쪽 서브트리순회
    if tree.left != None:
        result = result + inorder(tree.left)

    #2루트노드
    result.append(tree.index)

    #3오른쪽 서브트리순회
    if tree.right != None:
        result = result + inorder(tree.right)

    return result

def postorder(tree) :
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    #1왼쪽 서브트리순회
    if tree.left != None:
        result = result + postorder(tree.left)

    #2오른쪽 서브트리순회
    if tree.right != None:
        result = result + postorder(tree.right)
        
    #3루트노드
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
