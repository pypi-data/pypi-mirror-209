// Define the SIP wrapper to the hello library

%Module foolib

%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip

class  FooClass
{
%TypeHeaderCode
#include <fooclass.h>
%End

public:
    FooClass();
    QString Echo(QString s);
};

class FooMenu : public QWidget
{
%TypeHeaderCode
#include <fooclass.h>
%End

public:
    FooMenu(QWidget *parent /TransferThis/ = 0);
    ~FooMenu();
    
};
