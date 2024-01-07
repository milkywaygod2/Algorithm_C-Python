#include "__PCH.h"
#include "listPipe.h"
/*
3
1 0
2 1
3 0

3 1 2
*/
listPipe::listPipe()
{
}

listPipe::~listPipe()
{
}

std::vector<int> processBeads(std::vector<std::pair<int, int>> _vInput)
{
	listPipe myPipe;
	for (auto bead : _vInput) //:인자 자료형으로 자동설정 및 새로운 변수선언, pair<int,int>타입변수
	{
		if (bead.second == 0){
			myPipe.addLeft(bead.first);
		}
		else{
			myPipe.addRight(bead.first);
		}
	}
	std::vector<int> result(myPipe.getBeads().begin(), myPipe.getBeads().end());
	return result;
}
