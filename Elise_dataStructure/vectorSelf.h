#pragma once
class vectorSELF {
private:
    int* m_iNums;
    int m_iCapacity;
    int m_iSize;
public:
    void addNumber(int _i);
    void removeNumber(int _i);
    int getSize();
    int getNumber(int _iIndex);

public:
    vectorSELF();
    ~vectorSELF();
};
