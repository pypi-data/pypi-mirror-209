#include "dataviewer.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    dataviewer w;
    w.show();

    return a.exec();
}
