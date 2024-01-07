#pragma once

class LinkedlistElement
{
public:
	int value;
	LinkedlistElement* nextElement;
	//�߰��������� : value, nextElement �̹� ������ �ɹ����������� ����... �ܺ����ް� �����ϰ� �����ϱ� ����
	//�ʱ�ȭ : �����ڿ��� �ϴ� �ͺ��� ȿ������, �ʱ�ȭ�� �ɹ�����ȭ ������
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
	std::vector<int> processBeads(std::vector<std::pair<int, int>> _vPairInput); //result����

public:
	LinkedlistPipe() : m_start(nullptr), m_end(nullptr) {};
	~LinkedlistPipe() {};
};

