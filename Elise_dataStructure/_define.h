#pragma once

#define SINGLETON(type) \
public: static type* getInst() {static type func; return &func;}\
private: type(); ~type();
