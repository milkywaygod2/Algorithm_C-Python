#pragma once
#include "__PCH.h"

enum class Func{
    Add,
    Remove,
    GetMAX,
    Null,
};
struct tFunc{
    Func eFunc;
};
enum class With{
    VectorAlgorithm,
    Vector,
    None,
    Null,
};
struct tWith{
    With eWith;
};

//메인클래스
class machineMax {
private:
    std::vector<int> m_vNums;
    vectorSELF* m_vecSelf;
public:
    void example();
    int excute(const tFunc& _Func , const tWith& _With, int& _i);

public:
    machineMax();
    ~machineMax();
};

//1
class machineMax_VectorAlgoritm {
private:
    std::vector<int> m_vNums;
public:
    void addNumber(int _i);
    void removeNumber(int _i);
    int getMax();
};

//2
class machineMax_Vector {
private:
    std::vector<int> m_vNums;
public:
    void addNumber(int n);
    void removeNumber(int n);
    int getMax();
};

//3 자체구현 동적배열리스트 vectorSELF클래스 전제
class machineMax_None {
private:
    vectorSELF* m_vNums;
public:
    void addNumber(int n);
    void removeNumber(int n);
    int getMax();

};