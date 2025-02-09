#ifndef ITERATOR_H
#define ITERATOR_H

typedef int DATA;
class Iterater;

class Aggregate
{
public:
    virtual ~Aggregate(){}
    virtual Iterater* CreateIterater(Aggregate *pAggregate) = 0;
    virtual int GetSize() = 0;
    virtual DATA GetItem(int nIndex) = 0;
};

// 一个具体的容器类,这里是用数组表示
class ConcreateAggregate    : public Aggregate
{
public:
    ConcreateAggregate(int nSize);
    virtual ~ConcreateAggregate();
    virtual Iterater* CreateIterater(Aggregate *pAggregate);
    virtual int GetSize();
    virtual DATA GetItem(int nIndex);
private:
    int m_nSize;
    DATA *m_pData;
};

// 迭代器的抽象基类
class Iterater
{
public:
    virtual ~Iterater(){}

    virtual void First()        = 0;
    virtual void Next()         = 0;
    virtual bool IsDone()       = 0;
    virtual DATA CurrentItem()  = 0; 
};

// 访问ConcreateAggregate容器类的迭代器类
class ConcreateIterater : public Iterater
{
public:
    ConcreateIterater(Aggregate* pAggregate);
    virtual ~ConcreateIterater(){}

    virtual void First();
    virtual void Next();
    virtual bool IsDone();
    virtual DATA CurrentItem();
private:
    Aggregate  *m_pConcreateAggregate;
    int         m_nIndex;
};

#endif
