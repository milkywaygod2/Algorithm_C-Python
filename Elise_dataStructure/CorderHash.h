#pragma once
/*
HashTable(unorderedMap):�������� n^0���⵵
vs Map :�������� n^1���⵵
*/

class listElement2 {
private:

public:
	int data;
	listElement2* prev;
	listElement2* next;
public:
	listElement2(int _data):data(_data),prev(nullptr),next(nullptr) {}
	~listElement2() {}
};

class CorderHash {
private:
	
public:
	listElement2* m_head;
	listElement2* m_tail;
	std::unordered_map<int, listElement2*> dictionary; //�ڵ��ʱ�ȭ

	void addOrder(int _order);
	void eraseOrder(int _order);
	int getOrder(int _order);

public:
	CorderHash():m_head(nullptr), m_tail(nullptr) {}
	~CorderHash(){}
};

