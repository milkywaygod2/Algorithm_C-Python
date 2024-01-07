#pragma once
class CmachineMax {
private:
	std::vector<int> numbers;
public:
	void addNumber(int _i) { numbers.push_back(_i); }
	void eraseNumber(int _i) { numbers.erase(std::remove(numbers.begin(), numbers.end(), _i), numbers.end()); } 
	//remove : _i 전부뒤로이동시키고 마지막다음반복자반환
	//erase : ~,~ 까지 제거
	int getMax();
public:
	CmachineMax(){}
	~CmachineMax(){}
};

