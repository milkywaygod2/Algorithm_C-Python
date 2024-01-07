#include "__PCH.h"
/*
vectorSELF::vectorSELF()
    : capacity(1), size(0) {
    m_vNums = new int[capacity];
}
vectorSELF::~vectorSELF() {
    delete[] m_vNums;
}
*/

//vectorSELF
vectorSELF::vectorSELF()
    : m_iNums(0)
    , m_iCapacity(0)
    , m_iSize(0)
{
}

vectorSELF::~vectorSELF()
{
}


void vectorSELF::addNumber(int _i) {
    if (m_iSize == m_iCapacity) {
        int* temp = new int[2 * m_iCapacity];
        for (int i = 0; i < m_iSize; i++) {
            temp[i] = m_iNums[i];
        }
        delete[] m_iNums;
        m_iCapacity *= 2;
        m_iNums = temp;    }
    m_iNums[m_iSize++] = _i;}

void vectorSELF::removeNumber(int _i) {
    for (int i = 0; i < m_iSize; i++) {
        if (m_iNums[i] == _i) {
            for (int j = i; j < m_iSize - 1; j++) {
                m_iNums[j] = m_iNums[j + 1];
            }
            m_iSize--;
            break;        }    }}

int vectorSELF::getSize() {    
    return m_iSize;}

int vectorSELF::getNumber(int _iIndex) {    
    return m_iNums[_iIndex];}
