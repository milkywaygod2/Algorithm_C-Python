#pragma once
class CmachineMax {
private:
	std::vector<int> numbers;
public:
	void addNumber(int _i) { numbers.push_back(_i); }
	void eraseNumber(int _i) { numbers.erase(std::remove(numbers.begin(), numbers.end(), _i), numbers.end()); } 
	//remove : _i ���εڷ��̵���Ű�� �����������ݺ��ڹ�ȯ
	//erase : ~,~ ���� ����
	int getMax();
public:
	CmachineMax(){}
	~CmachineMax(){}
};

