
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

2 4
'''
def inorder(tree, depth):
    result=[]
    
    if tree.left != None:
        result += inorder(tree.left, depth + 1)

    tree.setDepth(depth)
    result.append(tree) #벡터에 저장하는 실제 객체는 요거 한줄이 끝.

    if tree.right != None:
        result += inorder(tree.right, depth + 1)

    return result

def getWidth(myTree) :
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    
    반환값 형식 : (l, w)
    '''
##트리생성_루트
    result = inorder(myTree, 1) #배열result는 깊이1부터시작

##트리사이즈데이터용_변수설정
    n = len(result)

    #깊이는 최대 1000가정 => 최대높이 1001 => 인덱스는 0~1001
    left =[1001 for i in range(1001)] # 0~1000인덱스로 원소는 전부 1001(불가능초기값, 오른쪽부터 왼쪽으로 꼼꼼히 검사)
    right = [-1 for i in range(1001)] # 0~1000인덱스로 원소는 전부 -1(불가능초기값, 왼쪽부터 오른쪽으로 꼼꼼히 검사)
    maxDepth = 0

##트리사이즈범위데이터_수집
    for i in range(n):      #i 검사중인 현재 노드의 위치
        d = result[i].depth #d 전위순회순서상의 현재 노드(i)의 깊이 (최대깊이1000가정)

        #결국 같은 깊이 d인 i들끼리 i vs i 로 재귀 비교하여 최종값을 각 배열의 같은 깊이 d 인덱스에 저장
        left[d] = min(left[d], i) #배열left의 인덱스d에 i값 저장, min(1001,i)으로 시작해서 재귀: 재귀후 1001인 인덱스=>원소존재X
        right[d] = max(right[d], i) #배열right의 인덱스d에 i값 저장, max(-1,i)으로 시작해서 재귀: 재귀후 -1인 인덱스=>원소존재X
        maxDepth = max(maxDepth, d) #최대깊이는 따로 기억 max(0,d)로 시작 재귀

##트리사이즈_측정
    widestDepth = 0
    widestLength = 0
    for d in range(1, maxDepth+1): #깊이d에 대해서 for문, 루트 자신을 포함

        width = right[d] - left[d] + 1 # 너비단위:몇노드, 깊이1인 루트에서는 right[1] = left[1]
        if widestLength < width:
            widestLength = width
            widestDepth = d #노드깊이
 
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