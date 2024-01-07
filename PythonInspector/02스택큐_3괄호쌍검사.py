
'''
�Է�
ù ��° �ٿ� ��ȣ ���ڷ� �̷���� ���ڿ� p�� �־����ϴ�. 
���ڿ� p�� ���̴� n�Դϴ�. 2��n��1000

(())())()
NO

(((())())(()())((())()))
YES
'''

class Stack:
    '''
    List�� �̿��Ͽ� ������ method���� �ۼ��ϼ���.
    '''
    def __init__(self) :
        '''
        �ڷḦ ������ ����(�迭) myStack�� ����ϴ�.
        '''
        self.myStack = []
        pass

    def push(self, n) :
        '''
        stack�� ���� n�� �ֽ��ϴ�.
        '''
        self.myStack.append(n)
        pass

    def pop(self) :
        '''
        stack���� ���� ���� �ִ� ������ �����մϴ�. 
        ���� stack�� �ƹ� ���Ұ� ���ٸ� �ƹ� �ϵ� ���� �ʽ��ϴ�.
        '''
        if  self.empty() == 1:
            return
        else:
            self.myStack.pop()
        pass

    def size(self) :
        '''
        stack�� ��� �ִ� ������ ������ return �մϴ�.
        '''
        return len(self.myStack)
        pass

    def empty(self) :
        '''
        stack�� ����ִٸ� 1, �ƴϸ� 0�� return �մϴ�.
        '''
        if self.size() == 0:
            return 1
        else:
            return 0
        pass

    def top(self) :
        '''
        stack�� ���� ���� �ִ� ������ return �մϴ�. 
        ���� stack�� ����ִ� ���� ���� ��쿡�� -1�� return �մϴ�.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myStack[-1] #���帶�������� ��ȯ
        pass

def checkParen(p) :
    '''
    ��ȣ ���ڿ� p�� ���� ������ "YES", �ƴϸ�  "NO"�� ��ȯ
    '''
    s = Stack()
    for c in p:
        if c == '(':
            s.push(c)
        else:
            if s.empty() == 1:
                return "NO"
            else:
                s.pop()
    if s.empty() ==1:
        return "YES"
    else:
        return "NO"

    return "NO"


def main():
    '''
    �׽�Ʈ�� ���� �ڵ��Դϴ�.
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


