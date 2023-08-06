#ifndef DATAVIEWER_H
#define DATAVIEWER_H

#include <QMainWindow>

namespace Ui {
class dataviewer;
}

class dataviewer : public QMainWindow
{
    Q_OBJECT

public:
    explicit dataviewer(QWidget *parent = 0);
    ~dataviewer();

private:
    Ui::dataviewer *ui;
};

#endif // DATAVIEWER_H
