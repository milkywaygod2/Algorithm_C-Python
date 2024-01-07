#include "__PCH.h"
#include "CorderList.h"

/*
10
1 4
1 8
3 8
1 2
1 1
2 4
3 8
1 59
1 5959
3 59

2
1
4

11
1 2
2 2
1 1818
1 8282
1 2255
1 6515
2 1818
1 486
3 486
3 3
1 4860

4
-1
*/
void CorderList::addOrder(int _order) {
	if(!m_head) {
		m_head = m_tail = new listElement1(_order);
	} else {
		m_tail->next = new listElement1(_order, m_tail);
		m_tail = m_tail->next;
	}
}

void CorderList::eraseOrder(int _order) {
	listElement1* current = m_head;
	while(current) {
		if(current->data == _order) {
			if(current->prev) {
				current->prev->next = current->next;
			} else {
				m_head = current->next;
			}
			if(current->next) {
				current->next->prev = current->prev;
			} else {
				m_tail = current->prev;
			}
			delete current;
			return;
		}
		current = current->next;
	}
}

int CorderList::getOrder(int _order) {
	listElement1* current = m_head;
	int index = 0;
	while(current) {
		if(current->data == _order) {
			return index + 1;
		}
		current = current->next;
		index++;
	}
	return -1;
}
