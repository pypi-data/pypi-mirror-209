#include "fooclass.h"


FooClass::FooClass(QObject *parent) :
QObject(parent)
{
}

QString FooClass::Echo(QString s)
{
    return s;
}


FooMenu::FooMenu(QWidget *parent) :
QWidget(parent)
{
    resize(250, 150);
    setWindowTitle("Simple");
}

FooMenu::~FooMenu()
{
}
