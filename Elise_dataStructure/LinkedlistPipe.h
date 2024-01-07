#pragma once

class LinkedlistElement
{
public:
	int value;
	LinkedlistElement* nextElement;
	//추가변수선언 : value, nextElement 이미 있지만 맴버변수용으로 생성... 외부전달값 안전하게 전달하기 위함
	//초기화 : 생성자에서 하는 것보다 효율적임, 초기화로 맴버변수화 시켜줌
	LinkedlistElement(int _val, LinkedlistElement* _ptr = nullptr) : value(_val), nextElement(_ptr) {} 
};

class LinkedlistPipe
{
private:

public:
	LinkedlistElement* m_start;
	LinkedlistElement* m_end;
	void addLeft(int _i);
	void addRight(int _i);
	std::deque<int> getBeads();
	std::vector<int> processBeads(std::vector<std::pair<int, int>> _vPairInput); //result포함

public:
	LinkedlistPipe() : m_start(nullptr), m_end(nullptr) {};
	~LinkedlistPipe() {};
};

