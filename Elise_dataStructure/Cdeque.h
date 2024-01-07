#pragma once
/*
vector : 동적배열->인덱스접근가능,왼쪽추가삭제-최악효율성 + 연속메모리 + 확장비용클수있음
deque : 동적선형구조(배열x)->인덱스접근가능,양쪽추가삭제-자유로움  + 가상메모리 + 확장비용절감
*/
class Cnode {
private:

public:
	int iData;
	Cnode* next;
	Cnode* prev;
public:
	Cnode(int _val):iData(_val),next(nullptr),prev(nullptr){}
	~Cnode(){}
};

//double-ended-queue
class Cdeque {
private:
	Cnode* m_front;
	Cnode* m_back;
	int m_count;
public:
	bool isEmpty(){ return(m_front == nullptr ); }
	void push_front(int _value);
	void push_back(int _value);
	void pop_front();
	void pop_back();
	int get_front();
	int get_back();
	int get_at(int _index);
	int size(){ return m_count; }
	void clear(){ while(!isEmpty()) { pop_front(); } }

public:
	Cdeque():m_front(nullptr), m_back(nullptr), m_count(0) {}
	~Cdeque(){}
};

