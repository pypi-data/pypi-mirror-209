#ifndef FOOLIB_H
#define FOOLIB_H

#include "FooLib_global.h"
#include <QtCore/QObject>
#include <QtCore/QString>
#include <QtGui/QWidget>

class FOOLIBSHARED_EXPORT FooClass : public QObject
{
    Q_OBJECT
public:
    FooClass(QObject *parent = 0);
    QString Echo(QString s);
};

class FOOLIBSHARED_EXPORT FooMenu : public QWidget
{
    Q_OBJECT

public:
    FooMenu(QWidget *parent=0);
    ~FooMenu();
    
};

#endif // FOOLIB_H
