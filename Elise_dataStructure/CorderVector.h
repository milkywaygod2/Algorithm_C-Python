#pragma once
class CorderVector {
private:
	std::vector<int> m_vData;
public:
	void addOrder(int _orderid) { m_vData.push_back(_orderid); }
	void eraseOrder(int _orderid) { m_vData.erase(std::remove(m_vData.begin(), m_vData.end(), _orderid), m_vData.end()); }
	int getOrder(int _orderid) {
		auto it = std::find(m_vData.begin(), m_vData.end(), _orderid);
		if(it != m_vData.end()) {
			return std::distance(m_vData.begin(), it) + 1;
		} else {
			return -1;
		}
	}
public:
	CorderVector(){}
	~CorderVector(){}
};

