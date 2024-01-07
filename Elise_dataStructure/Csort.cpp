#include "__PCH.h"
#include "Csort.h"
/*
2 5 1 4 4 3 2
5 4 4 3 2 2 1
*/
std::vector<int> Csort::sortDescend(std::vector<int>& _vList) {
    CmachineMax machineMax;
    std::vector<int> result;

    for(auto num : _vList) {
        machineMax.addNumber(num);          //정렬대상복사
    }
    while(machineMax.getMax() != -1) {
        int max_num = machineMax.getMax();  //옮기고
        result.push_back(max_num);          //정렬
        machineMax.eraseNumber(max_num);    //다옮긴건삭제
    }
    return result;
}
