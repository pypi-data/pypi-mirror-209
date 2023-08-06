#include "qrangeslider.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QRangeSlider w(Qt::Horizontal);
    w.show();

    return QApplication::exec();
}
