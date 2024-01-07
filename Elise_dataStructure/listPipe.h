#pragma once
class listPipe //�����ֱ�(�迭��Ÿ��)
{
private:

public:
	/*
	vector : �����迭->�ε������ٰ���,�����߰�����-�־�ȿ���� + ���Ӹ޸� + Ȯ����Ŭ������
	deque : ������������(�迭x)->�ε������ٰ���,�����߰�����-�����ο�  + ����޸� + Ȯ��������
	*/
	std::deque<int> m_iPipe;							//�����������̳�(������)
	void addLeft(int _i) { m_iPipe.push_front(_i); }	//�����߰�
	void addRight(int _i) { m_iPipe.push_back(_i); }	//�������߰�
	std::deque<int> getBeads() { return m_iPipe; }		//������ġ��ȯ

public:
	listPipe();
	~listPipe();
};

std::vector<int> processBeads(std::vector<std::pair<int, int>> _vInput); //��������ü����(���빰) <��������,����>


