'''
대칭 이진트리
주어진 이진트리가 좌우 대칭임을 판단하는 프로그램을 작성하시오. 예를 들어, 다음의 트리는 대칭이다.

입력
첫 번째 줄에 노드의 개수 n이 주어진다. 두 번째 줄에 n개의 숫자가 주어지며, 이는 각 노드의 값을 나타낸다. 
세 번째 줄부터 n개의 줄에 대하여 간선의 정보가 주어진다. 각 줄은 세 개의 숫자 a, b, c로 이루어 지며, 
이는 정점 a가 왼쪽 자식으로 b, 오른쪽 자식으로 c를 갖는다는 의미이다. 만약 갖는 자식노드가 없다면 -1이 주어진다.

출력
주어진 이진트리가 좌우 대칭이면 Yes, 아니면 No를 출력하는 프로그램을 작성하시오.

입력 예시 1
7
1 2 4 3 2 3 4
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 6
5 -1 -1
6 -1 -1

출력 예시 1
Yes

입력 예시 2
5
1 2 2 3 3
0 1 2
1 3 -1
2 4 -1
3 -1 -1
4 -1 -1

출력 예시 2
No
'''
def symmetricTree(tree, nodeValue):
    '''
    주어진 tree가 좌우 대칭이면 True, 아니면 False를 반환하는 함수.

    단, nodeValue[i] : Node i의 값을 나타내며, 
        tree[i][0] : Node i의 왼쪽 Node의 index,
        tree[i][1] : Node i의 오른쪽 Node의 index를 나타낸다.
        단, 자식 Node가 존재하지 않을 경우 index는 -1이다.

    '''

    result = True

    return result

#main.py
from symmetricTree import symmetricTree

def main():
    '''
    Do not change this code
    '''
    
    n = int(input())
    nodeValue = [int(x) for x in input().split()]
    tree = [ [] for x in range(n) ]

    for i in range(n) :
        line = [int(x) for x in input().split()]
        tree[line[0]].append(line[1])
        tree[line[0]].append(line[2])

    if(symmetricTree(tree, nodeValue) == True) :
        print("Yes")
    else :
        print("No")

if __name__ == "__main__":
    main()
