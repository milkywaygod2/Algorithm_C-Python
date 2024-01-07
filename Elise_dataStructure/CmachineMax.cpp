#include "__PCH.h"
#include "CmachineMax.h"
/*
9
0 1
0 2
0 4
0 5
2
1 5
2
1 2
2

5
4
4
*/
int CmachineMax::getMax() {
	if(numbers.empty()) {
		return -1;
	} else {
		return *std::max_element(numbers.begin(), numbers.end()); //max_element반환값 : max이터레이터
	}
}
