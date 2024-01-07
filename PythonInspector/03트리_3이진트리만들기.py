
'''
입력
첫 번째 줄에 노드의 개수를 나타내는 정수 n이 입력됩니다. (1≤n≤1000)
두 번째 줄부터 n줄에 걸쳐 정수 a b c가 공백으로 구분되어 입력됩니다.
정점 a가 왼쪽 자식으로 b, 오른쪽 자식으로 c를 갖는다는 의미입니다. 만약 노드의 자식 노드가 없다면 -1이 주어집니다.
단, 첫 번째로 주어지는 정점은 무조건 루트 노드가 입력되며 루트 노드가 갖는 값은 1입니다.
이외의 각 정점들은 이미 입력된 정점들 중 하나를 부모 노드로 갖는 경우만 입력됩니다.
즉 정점이 뒤죽박죽 입력되는 경우는 없습니다.

출력
Tree 클래스를 올바르게 작성해야 합니다.
Tree 클래스의 구현이 올바른지 확인하기 위하여 preorder, inorder, postorder 함수로부터 각각 전위, 중위, 후위 순회의 결과가 출력됩니다.

5
1 2 3
2 4 5
3 -1 -1
4 -1 -1
5 -1 -1

1 2 4 5 3
4 2 5 1 3
4 5 2 3 1

위처럼 정상적인 트리입력은 잘 들어가지만
1 2 3
4 5 6
7 8 9
와 같은 개연성없는 입력은 독립적인 트리객채만 만들뿐 연결이 없다.
'''


class Tree:
    #어떤 트리의 루트 노드를 갖고있다
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    #재귀적 특성
    # : 자식 if 현재 노드의 자식? else 자식중에 골라서 그 자식으로
    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        #루트노드 혹은 i노드자신에게 자식부여
        #직전addNode에서의 self.index값 vs 새로운 i
        if self.index == None or self.index == i:  
      
            self.index = i #새로운 i로 self.index업데이트

            #왼쪽객체
            self.left = Tree(l,None,None) if l != None else None 

            #오른쪽객체
            self.right = Tree(r,None,None) if r != None else None

            return True

        #자신의 자식에게 자식부여상황
        else:
            #flag가 참이 될 때까지 탐색
            flag = False

            #왼쪽자식있다면
            if self.left != None: 
                flag = self.left.addNode(i,l,r) #왼쪽객체에 addNode

            #왼쪽실패 오른자식있다면
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
