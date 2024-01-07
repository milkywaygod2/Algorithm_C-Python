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
        machineMax.addNumber(num);          //���Ĵ�󺹻�
    }
    while(machineMax.getMax() != -1) {
        int max_num = machineMax.getMax();  //�ű��
        result.push_back(max_num);          //����
        machineMax.eraseNumber(max_num);    //�ٿű�ǻ���
    }
    return result;
}
