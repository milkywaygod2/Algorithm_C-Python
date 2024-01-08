'''
학생들 사이의 친구관계가 myInput으로 주어질 때, 정원이가 퍼트린 소문을 듣게되는 학생의 수를 반환합니다.

이상한 소문
정원이는 같은 반 친구들에게 소문내는 것을 좋아합니다. 
자기가 하고 싶은 이야기를 주변 친구들에게 퍼뜨리는 것을 즐겨하는데, 소문은 친구의 친구를 통해서 빠르게 퍼져서 결국 연결된 친구들은 이를 모두 알게 됩니다.

그림 1
예를 들어 정원이네 반 학생 7명의 친구관계가 <그림 1>과 같다고 해봅시다. 이 그림에서 친구끼리는 연결선으로 연결되어 있고, 친구가 아니면 연결되어 있지 않습니다. 
이 네트워크 상에서 정원이가 1번이라면, 소문은 2번과 5번 친구를 거쳐 결과적으로 2, 3, 5, 6번 학생이 소문을 듣게 됩니다. 하지만, 4번과 7번 학생은 이들과 친구가 아니기 때문에 소문을 들을 수 없습니다.
정원이가 1번이라고 가정할 때, 같은 반 학생(노드) 수와 친구관계(간선) 정보가 주어질 때, 정원이에 의해서 이야기를 듣게 되는 학생 수를 구하는 프로그램을 작성하세요.

입력
첫째 줄에는 같은 반 학생 수가 주어집니다. 학생 수는 30명 이하이고, 학생에게는 1번부터 차례로 번호가 매겨집니다.
둘째 줄에는 학생 연결망 상에서 친구관계를 나타내는 순서쌍의 수가 주어집니다. 그 다음에는 차례로 연결망에서 연결된 실제 순서쌍이 주어집니다.

출력
정원(1번 노드)이가 퍼트린 소문을 듣게 되는 학생의 수를 출력합니다.

입력 예시
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력 예시
4
'''
import sys
sys.setrecursionlimit(100000)

def numStudents(n_nodes,myInput) :
 
    result = 0

    return result 

#main.py
import sys
sys.setrecursionlimit(100000)

def main():
    '''
    Do not change this code
    '''
    n_nodes = int(input())
    m_edges = int(input())

    myInput = []

    for i in range(m_edges) :
        line = [int(x) for x in input().split()]
        myInput.append(line)

    print(numStudents(n_nodes,myInput))

if __name__ == "__main__":
    main()

