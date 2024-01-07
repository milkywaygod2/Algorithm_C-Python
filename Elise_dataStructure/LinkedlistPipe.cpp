#include "__PCH.h"
#include "LinkedlistPipe.h"
/*
3
1 0
2 1
3 0

3 1 2
*/
void LinkedlistPipe::addLeft(int _i) {
	if (m_start == nullptr && m_end == nullptr) {
		m_start = m_end = new LinkedlistElement(_i);
	}
	else {
		LinkedlistElement* new_element = new LinkedlistElement(_i, m_start); //����������(nullptr)
		m_start = new_element;
	}
} //���ο������

void LinkedlistPipe::addRight(int _i) {
	if (m_start == nullptr && m_end == nullptr) {
		m_start = m_end = new LinkedlistElement(_i);
	}
	else {
		LinkedlistElement* new_element = new LinkedlistElement(_i);
		m_end->nextElement = new_element; //����������ptr
		m_end = new_element;
	}
} //���ο��

std::deque<int> LinkedlistPipe::getBeads() {
	std::deque<int> dBeads;
	LinkedlistElement* current = m_start;
	while (current != nullptr) {
		dBeads.push_back(current->value);
		current = current->nextElement;
	}
	return dBeads;
}

std::vector<int> LinkedlistPipe::processBeads(std::vector<std::pair<int, int>> _vPairInput) {
	LinkedlistPipe myPipe;
	for (auto Bead : _vPairInput) {
		if (Bead.second == 0) {
			myPipe.addLeft(Bead.first);
		}
		else {
			myPipe.addRight(Bead.first);
		}
	}
	std::vector<int> result ( myPipe.getBeads ( ).begin ( ) , myPipe.getBeads ( ).end ( ) );
	return result;
}
