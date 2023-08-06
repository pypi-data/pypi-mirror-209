#include "dataviewer.h"
#include "ui_dataviewer.h"

dataviewer::dataviewer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::dataviewer)
{
    ui->setupUi(this);
}

dataviewer::~dataviewer()
{
    delete ui;
}
