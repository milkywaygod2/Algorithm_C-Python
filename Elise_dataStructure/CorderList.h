#pragma once
class listElement1 {
private:

public:
	int data;
	listElement1* prev;
	listElement1* next;
public:
	listElement1(int _data, listElement1* _prev = nullptr, listElement1* _next = nullptr):data(_data),prev(_prev),next(_next){}
};

class CorderList {
private:
	listElement1* m_head;
	listElement1* m_tail;
public:
	void addOrder(int _order);
	void eraseOrder(int _order);
	int getOrder(int _order);
public:
	CorderList():m_head(nullptr), m_tail(nullptr){}
	~CorderList(){}
};

