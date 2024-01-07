#include "__PCH.h"
#include "Cstack.h"

/*
�Է�
ù ��° �ٿ� ���̰� n�� ��ȣ ���ڿ� p�� �־����ϴ�.2��n��20000
�־����� ���ڿ� p�� �׻� �ùٸ� ��ȣ ���ڿ��Դϴ�. ��, ��)(���̳� ��())�� �� ���� �Է��� �־����� �ʽ��ϴ�.
((((())((())()))())())

11 9 7 2 1 1 2 6 4 3 3 4 5 5 6 7 8 8 9 10 10 11
*/
std::vector<int> Cstack::order_paren(std::string _parentheses) {
	{ //parenthesis�� �ܼ� : ��ȣ���
		Cstack myStack; //std::stack<int> myStack;
		std::vector<int> iVresult(_parentheses.length(), 0); //0�ʱ�ȭ
		int iParen = 1;

		for(int iPush = 0; iPush < _parentheses.length(); iPush++) {
			if(_parentheses[iPush] == '(') {
				myStack.push(iPush);
			} else if(_parentheses[iPush] == ')') {
				if(myStack.empty()) {
					throw std::runtime_error("Failed");
				} else {
					int iPop = myStack.top(); //���� �ֽ� ( �ε�����ȣ�� ��ȸ
					myStack.pop();
					iVresult[iPush] = iParen;//�ش��ε�����ȣ�� ��� ���� )�� paren�������Է�
					iVresult[iPop] = iParen; //�ش��ε�����ȣ�� ���� ���� ¦ (�� paren�������Է�
					++iParen;
				}
			}
		}
		return iVresult;
	}
}
void Cstack::IO_order_paren() {
}

/*
���û���
ù ��° �ٿ� �׽�Ʈ ���̽��� ������ �ǹ��ϴ� ���� T�� �Էµ˴ϴ�. (1��T��10)
�� ��° �ٺ��� T���� �ٿ� ����, �� �ٸ��� �׽�Ʈ ���̽��� �ϳ��� �Էµ˴ϴ�.
�� �׽�Ʈ ���̽��� ������ ��Ģ���� ���� �� �ִ��� �Ǻ��ؾ� �ϴ� ������ �־�����, ������ �� ���� �������� ���е˴ϴ�.
������ ũ�⸦ N�̶�� �Ѵٸ�, ������ �̷�� �ִ� �� ���� 1 �̻� N ������ �ڿ����̸� ���� ������ �ߺ����� �ʽ��ϴ�.
4
1 6 5 4 3 2
2 1 3 4
3 1 2 4
1 4 3 2 6 5 7 8

Yes
Yes
No
Yes
*/
std::string Cstack::is_iVstack(std::vector<int> _iVnums) {

	//Q.�������� ó���� ������ �����ΰ�?(�۾�������)
	//ex)_iVnums�� [2,7,4,1]

	Cstack myStack;	
	int numsIndex = 0; //Ȯ���Ϸ��� ��(�����ε���)
	myStack.push(1);

	//(1) ex..[2,4,3,1,5]�� ~.size���� ������� pop or push ������
	for(int myIndex = 2; myIndex <= _iVnums.size(); myIndex++) {
	
		//(2) pop ���� : ������ ��������ʰ� ������ ������ Ȯ���Ϸ��� ���� ���� ���
		while(!myStack.empty() && myStack.top() == _iVnums[numsIndex]) {
			myStack.pop();
			numsIndex++; //(3) ���� ���� ����
		}
		//(4) push ���� : ������ ����ְų� ������ ������ Ȯ���Ϸ��� ������ ���� ���
		if(myStack.empty() || myStack.top() < _iVnums[numsIndex]) {
			myStack.push(myIndex);
		} else {
			//(5) ������ ������ Ȯ�� ������ ū ��� => �������δ� push�� pop�� �Ұ����ϹǷ� ��������
			return "No";
			numsIndex = 0; //Ȯ���Ϸ��� ��(�����ε���)
			while(!myStack.empty()) {
				myStack.pop();
			}
			myStack.push(1);
		}
	}
	//(6) for�� �ٵ��� �����Ϸ� (myStack.empty()���� ����)
	return "Yes";
	numsIndex = 0; //Ȯ���Ϸ��� ��(�����ε���)
	while(!myStack.empty()) {
		myStack.pop();
	}
	myStack.push(1);
}
void Cstack::IO_is_iVstack() {
	//1.ù°�ٿ� �׽�Ʈ���̽� ���� n��
	//2.��°�ٺ��� n���� �ٿ� ���� �׽�Ʈ���̽� �ϳ��� �Է�
	int n;
	std::cin >> n;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::vector<std::string> sVresult;

	for(int i = 0; i < n; i++) { //1����
		std::vector<int> iVinputNums;
		std::string sNums;
		std::getline(std::cin, sNums);
		std::stringstream ssNums(sNums);
		int eachNum;
		while(ssNums >> eachNum) { //2����
			iVinputNums.push_back(eachNum);
		}
		sVresult.push_back(is_iVstack(iVinputNums));
	}
	for(auto &result_line_by_line : sVresult) {
		std::cout << result_line_by_line << std::endl;
	}
}

/*
�Է�
ù ��° �ٿ� �޸��忡 ó�� ����Ǿ� �ִ� ���ڿ� s�� �Է��մϴ�.
�� ��° �ٿ� �޸��忡 �Է��� ��ɾ��� ������ ���� n�� �Է��մϴ�. (1��n��10000)
�� ��° �ٺ��� n���� �ٿ� ���ļ� ��ɾ ���� �Էµ˴ϴ�.
abcdef
3
P g
L
P z

abcdefzg
*/
std::string Cstack::note_string(const std::string& _s, const std::vector<std::string>& _sVcmds) {
	std::vector<char> cVleft(_s.begin(), _s.end());
	std::vector<char> cVright;

	//vector�� ���� for��, 
	//����cmd�� vector�� ������ string������ ���� �ε���
	for(const auto& cmd : _sVcmds) { 
		if(cmd[0] == 'L') {
			if(!cVleft.empty()) {
				cVright.push_back(cVleft.back());
				cVleft.pop_back();
			}
		} else if(cmd[0] == 'R') {
			if(!cVright.empty()) {
				cVleft.push_back(cVright.back());
				cVright.pop_back();
			}
		} else if(cmd[0] == 'D') {
			if(!cVleft.empty()) {
				cVleft.pop_back();
			}
		} else if(cmd[0] == 'P') {
			cVleft.push_back(cmd[2]); //P g ��������� 2
		}
	}
	std::string result(cVleft.begin(), cVleft.end());
	std::reverse(cVright.begin(), cVright.end());
	result.append(cVright.begin(), cVright.end());
	return result;
}
void Cstack::IO_note_string() {
	std::string _s;
	std::cin >> _s;

	int _n;
	std::cin >> _n;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	std::vector<std::string> sVcmds(_n); //�޸�����!
	for(int i = 0; i < _n; i++) {
		std::getline(std::cin, sVcmds[i]);
	}
	std::cout << note_string(_s, sVcmds) << std::endl;
	
}



