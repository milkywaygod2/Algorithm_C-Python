#pragma once
class Cqueue {
private:
	std::deque<int> iDque;
public:
	void push(int _i) { iDque.push_back(_i); }
	void pop() { if(!emtpy()) { iDque.pop_front(); } }
	int size() { return iDque.size(); }
	bool emtpy() { return iDque.empty(); }

	int front() { if(emtpy()) { return-1; } else { return iDque.front(); } }
	int back() { if(emtpy()) { return-1; } else { return iDque.back(); } }

	//주문처리(접수-소요시간,우선처리)
	
	//요세푸스순열


public:
	Cqueue() { iDque.clear(); }
	~Cqueue(){}
};

