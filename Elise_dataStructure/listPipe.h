#pragma once
class listPipe //구슬넣기(배열스타일)
{
private:

public:
	/*
	vector : 동적배열->인덱스접근가능,왼쪽추가삭제-최악효율성 + 연속메모리 + 확장비용클수있음
	deque : 동적선형구조(배열x)->인덱스접근가능,양쪽추가삭제-자유로움  + 가상메모리 + 확장비용절감
	*/
	std::deque<int> m_iPipe;							//파이프컨테이너(껍데기)
	void addLeft(int _i) { m_iPipe.push_front(_i); }	//왼쪽추가
	void addRight(int _i) { m_iPipe.push_back(_i); }	//오른쪽추가
	std::deque<int> getBeads() { return m_iPipe; }		//구슬배치반환

public:
	listPipe();
	~listPipe();
};

std::vector<int> processBeads(std::vector<std::pair<int, int>> _vInput); //파이프객체생성(내용물) <넣을숫자,방향>


