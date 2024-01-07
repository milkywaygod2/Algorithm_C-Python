#include "__PCH.h"

//machineMax_withoutALL::machineMax_withoutALL() : m_vecSelf(new vectorSELF()) {}
//machineMax_withoutALL::~machineMax_withoutALL() { delete m_vecSelf; }

machineMax::machineMax() {}
machineMax::~machineMax() {}


//1함수상세
void machineMax_VectorAlgoritm::addNumber(int _i){
    m_vNums.push_back(_i);}
void machineMax_VectorAlgoritm::removeNumber(int _i){
    m_vNums.erase(std::remove(m_vNums.begin(), m_vNums.end(), _i), m_vNums.end());}
int machineMax_VectorAlgoritm::getMax(){
    if (m_vNums.empty()) {
        return -1;  // or any other value indicating an error
    }
    else {
        return *std::max_element(m_vNums.begin(), m_vNums.end());    }}

//2함수상세
void machineMax_Vector::addNumber(int n) {
    m_vNums.push_back(n);}
void machineMax_Vector::removeNumber(int n) {
    for (int i = 0; i < m_vNums.size(); i++) {
        if (m_vNums[i] == n) {
            m_vNums.erase(m_vNums.begin() + i);
            break;        }    }}
int machineMax_Vector::getMax() {
    if (m_vNums.empty()) {
        return -1;    }// or any other value indicating an error
    else {
        int max_val = m_vNums[0];
        for (int i = 1; i < m_vNums.size(); i++) {
            if (m_vNums[i] > max_val) {
                max_val = m_vNums[i];            }        }
        return max_val;    }}

//3함수상세
void machineMax_None::addNumber(int n) {
    m_vNums->addNumber(n);}
void machineMax_None::removeNumber(int n) {
    m_vNums->removeNumber(n);}
int machineMax_None::getMax() {
    int size = m_vNums->getSize();
    if (size == 0) {
        return -1;
    }  // or any other value indicating an error
    else {
        int max_val = m_vNums->getNumber(0);
        for (int i = 1; i < size; i++) {
            int num = m_vNums->getNumber(i);
            if (num > max_val) {
                max_val = num;            }        }
        return max_val;    }}

//함수실행 경우의수
int machineMax::excute(const tFunc& _Func, const tWith& _With, int& _i)
{
    int size = 0; //스위치문 안에서 초기화 하면안됨.
    int num = 0;
    int* nums = new int[size];

    int max_val = NULL;
    switch (_With.eWith)
    {
    //1벡터,알고리즘사용
    case With::VectorAlgorithm:
        switch (_Func.eFunc){
        case Func::Add:
            m_vNums.push_back(_i);
            printf("we-add-[%d]-to-machine\n", _i);
            break;
        case Func::Remove:
            m_vNums.erase(std::remove(m_vNums.begin(), m_vNums.end(), _i), m_vNums.end());
            break;
        case Func::GetMAX:
            if (m_vNums.empty()) { printf("empty!"); }
            else { max_val = *std::max_element(m_vNums.begin(), m_vNums.end());}
            break;
        default:
            printf("wrong-FUNCTION-try-again\n");
            break;}

    //2벡터사용
    case With::Vector:
        switch (_Func.eFunc){
        case Func::Add:
            m_vNums.push_back(_i);
            printf("we-add-[%d]-to-machine\n", _i);
            break;
        case Func::Remove:
            for (int i = 0; i < m_vNums.size(); i++) {
                if (m_vNums[i] == _i) {
                    m_vNums.erase(m_vNums.begin() + i); break;}}
            printf("we-remove-[%d]-from-machine\n", _i);
            break;
        case Func::GetMAX:
            if (m_vNums.empty()) { printf("empty!"); }
            else {
                max_val = m_vNums[0];
                for (int i = 1; i < m_vNums.size(); i++) {
                    if (m_vNums[i] > max_val) {
                        max_val = m_vNums[i];}}
                return max_val;}        
            break;
        default:
            printf("wrong-FUNCTION-try-again\n");
            break;}
        return max_val;

    //3하드코딩
    case With::None:
        switch (_Func.eFunc){
        case Func::Add:
            m_vecSelf->addNumber(_i);
            printf("we-add-[%d]-to-machine\n",_i);
            break;
        case Func::Remove:
            m_vecSelf->removeNumber(_i);
            printf("we-remove-[%d]-from-machine\n",_i);
            break;
        case Func::GetMAX:
            size = m_vecSelf->getSize();

            if (size == 0) { printf("empty!"); }
            else {
                max_val = m_vecSelf->getNumber(0);
                //nums[0] = max_val;
                if (size == 1){
                    nums[0] = num;
                }
                else if (size == 0){;}
                else
                {
                    //배열복사 : 
                    for (int i = 1; i < size; i++) {
                        num = m_vecSelf->getNumber(i);
                        nums[i] = num;
                        /*if (num > max_val) {
                            max_val = num;}}
                    return max_val;*/
                    }
                    //정렬 : j 앞부터 끝으로, i로 이미한 j끝은 패스
                    for (int i = 0; i < size - 1; i++) {
                        for (int j = 0; j < size - 1 - i; j++) {
                            if (nums[j] > nums[j + 1]) {
                                int temp = nums[j];
                                nums[j] = nums[j + 1];
                                nums[j + 1] = temp;
                            }
                        }
                    }
                }
            }
            max_val = nums[size - _i];
            delete[] nums;
            printf("we-found-max-number : %d",max_val);            
            break;
        default:
            printf("wrong-FUNCTION-try-again\n");
            break;}
    //엉뚱한입력..
    default:
        printf("wrong-LIBRARY-try-again\n");
        break;
    }
    if (max_val)
        return max_val;
}

//시연용
void machineMax::example(){
    tFunc _Func;
    _Func.eFunc = Func::Add;
    tWith _With;
    _With.eWith = With::VectorAlgorithm;

    int length = 10;
    for (int i = 0; i < length; i++){
        excute(_Func, _With, i);
    }

    char insertedFunc[10];
    char insertedLib[10];
    int insertedNum;
    printf("Enter this \n\n Function<Add|Remove|GetMax> \n Library<VectorAlgorithm|Vector|None> \n Number \n : ");
   
    //while (true){
        scanf_s("%s %s %d" , insertedFunc, (unsigned)_countof(insertedFunc), insertedLib, (unsigned)_countof(insertedLib), &insertedNum);
        //getchar();

        // "Add", "Remove", "GetMAX" 문자열을 tFunc 열거형으로 변환
        switch (insertedFunc[0]) {
        case 'A':
            _Func.eFunc = Func::Add;
            break;
        case 'R':
            _Func.eFunc = Func::Remove;
            break;
        case 'G':
            _Func.eFunc = Func::GetMAX;
            break;
        default:
            _Func.eFunc = Func::Null;
            printf("Invalid Func value. Try again.\n");
            break;
        }

        // "VectorAlgoritum", "Vector", "None" 문자열을 tWith 열거형으로 변환
        switch (insertedLib[0]) {
        case 'V':
            _With.eWith = With::VectorAlgorithm;
            break;
        case 'E':
            _With.eWith = With::Vector;
            break;
        case 'N':
            _With.eWith = With::None;
            break;
        default:
            _With.eWith = With::Null;
            printf("Invalid Lib value. Try again.\n");
            break;
        }

        excute(_Func, _With, insertedNum);
        if (_Func.eFunc == Func::GetMAX && !(_With.eWith == With::Null)) {
            int max_val = excute(_Func, _With, insertedNum);
            printf("max number is %d\n", max_val);
        }
    //}
}