#include "__PCH.h"
#include "Cstack.h"

/*
입력
첫 번째 줄에 길이가 n인 괄호 문자열 p가 주어집니다.2≤n≤20000
주어지는 문자열 p는 항상 올바른 괄호 문자열입니다. 즉, ‘)(‘이나 ‘())’ 과 같은 입력은 주어지지 않습니다.
((((())((())()))())())

11 9 7 2 1 1 2 6 4 3 3 4 5 5 6 7 8 8 9 10 10 11
*/
std::vector<int> Cstack::order_paren(std::string _parentheses) {
	{ //parenthesis는 단수 : 괄호요소
		Cstack myStack; //std::stack<int> myStack;
		std::vector<int> iVresult(_parentheses.length(), 0); //0초기화
		int iParen = 1;

		for(int iPush = 0; iPush < _parentheses.length(); iPush++) {
			if(_parentheses[iPush] == '(') {
				myStack.push(iPush);
			} else if(_parentheses[iPush] == ')') {
				if(myStack.empty()) {
					throw std::runtime_error("Failed");
				} else {
					int iPop = myStack.top(); //남은 최신 ( 인덱스번호를 조회
					myStack.pop();
					iVresult[iPush] = iParen;//해당인덱스번호에 방금 넣은 )의 paren계산순서입력
					iVresult[iPop] = iParen; //해당인덱스번호에 전에 넣은 짝 (의 paren계산순서입력
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
지시사항
첫 번째 줄에 테스트 케이스의 개수를 의미하는 정수 T가 입력됩니다. (1≤T≤10)
두 번째 줄부터 T개의 줄에 걸쳐, 각 줄마다 테스트 케이스가 하나씩 입력됩니다.
각 테스트 케이스는 문제의 규칙으로 만들 수 있는지 판별해야 하는 수열이 주어지며, 수열의 각 수는 공백으로 구분됩니다.
수열의 크기를 N이라고 한다면, 수열을 이루고 있는 각 수는 1 이상 N 이하의 자연수이며 수열 내에서 중복되지 않습니다.
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

	//Q.스택으로 처리가 가능한 수열인가?(작업순서등)
	//ex)_iVnums에 [2,7,4,1]

	Cstack myStack;	
	int numsIndex = 0; //확인하려는 수(스택인덱스)
	myStack.push(1);

	//(1) ex..[2,4,3,1,5]를 ~.size까지 순서대로 pop or push 했을때
	for(int myIndex = 2; myIndex <= _iVnums.size(); myIndex++) {
	
		//(2) pop 조건 : 스택이 비어있지않고 마지막 스택이 확인하려는 수와 같은 경우
		while(!myStack.empty() && myStack.top() == _iVnums[numsIndex]) {
			myStack.pop();
			numsIndex++; //(3) 다음 숫자 검토
		}
		//(4) push 조건 : 스택이 비어있거나 마지막 스택이 확인하려는 수보다 작은 경우
		if(myStack.empty() || myStack.top() < _iVnums[numsIndex]) {
			myStack.push(myIndex);
		} else {
			//(5) 마지막 스택이 확인 수보다 큰 경우 => 스택으로는 push나 pop이 불가능하므로 검증실패
			return "No";
			numsIndex = 0; //확인하려는 수(스택인덱스)
			while(!myStack.empty()) {
				myStack.pop();
			}
			myStack.push(1);
		}
	}
	//(6) for문 다돌면 검증완료 (myStack.empty()여부 무관)
	return "Yes";
	numsIndex = 0; //확인하려는 수(스택인덱스)
	while(!myStack.empty()) {
		myStack.pop();
	}
	myStack.push(1);
}
void Cstack::IO_is_iVstack() {
	//1.첫째줄에 테스트케이스 개수 n개
	//2.둘째줄부터 n개의 줄에 걸쳐 테스트케이스 하나씩 입력
	int n;
	std::cin >> n;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::vector<std::string> sVresult;

	for(int i = 0; i < n; i++) { //1실행
		std::vector<int> iVinputNums;
		std::string sNums;
		std::getline(std::cin, sNums);
		std::stringstream ssNums(sNums);
		int eachNum;
		while(ssNums >> eachNum) { //2실행
			iVinputNums.push_back(eachNum);
		}
		sVresult.push_back(is_iVstack(iVinputNums));
	}
	for(auto &result_line_by_line : sVresult) {
		std::cout << result_line_by_line << std::endl;
	}
}

/*
입력
첫 번째 줄에 메모장에 처음 저장되어 있는 문자열 s를 입력합니다.
두 번째 줄에 메모장에 입력할 명령어의 개수인 정수 n을 입력합니다. (1≤n≤10000)
세 번째 줄부터 n개의 줄에 걸쳐서 명령어가 각각 입력됩니다.
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

	//vector에 대한 for문, 
	//변수cmd는 vector의 인자인 string각각에 대한 인덱스
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
			cVleft.push_back(cmd[2]); //P g 띄어쓰기다음은 2
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

	std::vector<std::string> sVcmds(_n); //메모리절약!
	for(int i = 0; i < _n; i++) {
		std::getline(std::cin, sVcmds[i]);
	}
	std::cout << note_string(_s, sVcmds) << std::endl;
	
}



