#pragma once
class Cstack {
private:
	std::vector<int> m_iVstack; //stack���� �ص���
	//std::stack<int> iSstack; //�̷���
public:
	void push(int _i) { m_iVstack.push_back(_i); }
	void pop() { if(!empty()) { m_iVstack.pop_back(); } }
	int size() { return m_iVstack.size(); }
	bool empty() { return m_iVstack.empty(); }

	int top() { if(empty()) { return printf("this is empty"); } else { return m_iVstack.back(); } } //stack�� top

	//��ȣ¦�˻�

	//�켱����ȣ�˻�
	std::vector<int> order_paren(std::string _parentheses); //��ȣ¦���߱� ex (()((()())())) => 71164223345567
	void IO_order_paren();

	//���ü����˻�
	std::string is_iVstack(std::vector<int> _iVnums);
	void IO_is_iVstack();

	//�޸���
	std::string note_string(const std::string& _s, const std::vector<std::string>& _sVcommands);
	void IO_note_string();

public:
	Cstack() { m_iVstack.clear(); }
	~Cstack(){}
};