#include "__PCH.h"
#include "Cdeque.h"

void Cdeque::push_front(int _value) {
	Cnode* temp = new Cnode(_value);
	if(m_front = nullptr) {
		m_front = m_back = temp;
	} else {
		m_front->prev = temp; //��������Ʈ�տ� ����
		temp->next = m_front; //��������Ʈ�� �����ڷ�
		m_front = temp; //������ ���ο�����Ʈ�� (��������Ʈ�� �����ڿ�)
	}
}

void Cdeque::push_back(int _value) {
	Cnode* temp = new Cnode(_value);
	if(m_back = nullptr) {
		m_back = m_front = temp;
	} else {
		m_back->next = temp;
		temp->prev = m_back;
		m_back = temp;
	}
}

void Cdeque::pop_front() {
	if(isEmpty()) {//�� ��
		std::cout << "deque-underflow\n";
		return;
	}
	Cnode* temp = m_front; //�ɹ�������ü�� ��Ȱ���� �ؾ������� �ٷ� ������������ �Űܼ� ����
	m_front = m_front->next; //�ڿ��� ������ �����
	if(m_front == nullptr) { //���� ���Ұ� �� 1�� �־��� ��� = �� �� �����Ϸ��� ������ ���ܿ��� nullptr
		m_back == nullptr;
	}
	delete temp;
}

void Cdeque::pop_back() {
	if(isEmpty()) {
		std::cout << "deque-underflow";
		return;
	}
	Cnode* temp = m_back;
	m_back = m_back->prev;
	if(m_back == nullptr) {
		m_front == nullptr;
	}
	delete temp;
}

int Cdeque::get_front() {
	if(isEmpty()) {
		std::cout << "deque-underflow\n";
		return -1;
	}
	return m_front->iData;
}

int Cdeque::get_back() {
	if(isEmpty()) {
		std::cout << "deque-underflow\n";
		return -1;
	}
	return m_back->iData;
}

int Cdeque::get_at(int _index) {
	if(_index >= m_count || _index < 0) {
		std::cout << "Index out of range\n";
		return -1;
	}
	Cnode* temp = m_front;
	for(int i = 0; i < _index; i++) {
		temp = temp->next;
	}
	return temp->iData;
}
