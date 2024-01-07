#pragma once
/*
vector : �����迭->�ε������ٰ���,�����߰�����-�־�ȿ���� + ���Ӹ޸� + Ȯ����Ŭ������
deque : ������������(�迭x)->�ε������ٰ���,�����߰�����-�����ο�  + ����޸� + Ȯ��������
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

