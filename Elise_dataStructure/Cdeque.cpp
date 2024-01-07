#include "__PCH.h"
#include "Cdeque.h"

void Cdeque::push_front(int _value) {
	Cnode* temp = new Cnode(_value);
	if(m_front = nullptr) {
		m_front = m_back = temp;
	} else {
		m_front->prev = temp; //기존프론트앞에 템프
		temp->next = m_front; //기존프론트를 템프뒤로
		m_front = temp; //템프를 새로운프론트로 (기존프론트는 템프뒤에)
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
	if(isEmpty()) {//빈 덱
		std::cout << "deque-underflow\n";
		return;
	}
	Cnode* temp = m_front; //맴버변수자체는 재활용을 해야함으로 바로 삭제하지말고 옮겨서 삭제
	m_front = m_front->next; //뒤에것 앞으로 떙기기
	if(m_front == nullptr) { //덱에 원소가 딱 1개 있었던 경우 = 한 개 삭제하려고 빼놓고 땅겨오니 nullptr
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
