#include "__PCH.h"
#include "CorderHash.h"

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

void CorderHash::addOrder(int _order) {
	listElement2* new_order = new listElement2(_order);
	dictionary[_order] = new_order;

	if(!m_head) {
		m_head = m_tail = new_order;
	} else {
		new_order->prev = m_tail;
		m_tail->next = new_order;
		m_tail = new_order;
	}
}

void CorderHash::eraseOrder(int _order) {
	if(!m_head && !m_tail) {
		return;	}

	listElement2* current = dictionary[_order];

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

	dictionary.erase(_order); //¡Ú
}

int CorderHash::getOrder(int _order) {
	listElement2* current = m_head;
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
