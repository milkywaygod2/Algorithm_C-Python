'''
문자열 data가 주어질 때, 최소의 문자를 제거하여 만든 팰린드롬을 반환하는 함수를 작성하세요.

팰린드롬 구하기
팰린드롬이란, 앞으로 읽으나 뒤로 읽으나 똑같은 문자열을 말한다. 예를 들어, “aba”, “abdba”, “abffba” 는 모두 팰린드롬이다.
임의의 문자열이 주어질 때, 몇 개의 문자를 적당히 삭제하면 이를 팰린드롬으로 만들 수 있다. 
예를 들어, “abca”가 주어질 경우, 알파벳 ‘b’를 삭제하면 “aca”가 되므로, 팰린드롬으로 만들 수 있다.
임의의 문자를 제거함으로써 주어진 문자열을 팰린드롬으로 만들고 싶다고 할 때, 최종적으로 얻은 팰린드롬을 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 문자열이 주어진다. 문자열의 길이는 3000을 넘지 않는다.

출력
최종적으로 얻은 팰린드롬을 출력한다. 만약 그 팰린드롬이 여러가지라면, 그 중 하나만 출력해도 된다.

입력 예시 1
abcfba

출력 예시 1
abcba

입력 예시 2
abcdefg

출력 예시 2
a
'''
import sys
sys.setrecursionlimit(10000)

def getPalindrome(data) :

    return ""

#main.py
import sys
sys.setrecursionlimit(10000)
def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    s = input()

    print(getPalindrome(s))

if __name__ == "__main__":
    main()
