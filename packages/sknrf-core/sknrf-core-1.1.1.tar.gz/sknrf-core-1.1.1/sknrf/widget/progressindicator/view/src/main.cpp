#include <QApplication>
#include <QtGui/QtGui>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QFrame>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>

#include "qprogressindicator.h"

int main(int argc, char ** argv)
{
    QApplication app(argc, argv);

    auto * mw = new QMainWindow;

    auto* pi = new QProgressIndicator();

    auto* frame = new QFrame;

    auto* vbl = new QVBoxLayout;

    auto* startPb = new QPushButton("start spin");
    QObject::connect(startPb, SIGNAL(clicked(bool)), pi, SLOT(startAnimation()));

    auto* stopPb = new QPushButton("stop spin");
    QObject::connect(stopPb, SIGNAL(clicked(bool)), pi, SLOT(stopAnimation()));

    auto* delaySlider = new QSlider;
    delaySlider->setRange(0, 100);
    delaySlider->setValue(pi->animationDelay());
    delaySlider->setOrientation(Qt::Horizontal);
    QObject::connect(delaySlider, SIGNAL(valueChanged(int)), pi, SLOT(setAnimationDelay(int)));

    vbl->addWidget(startPb);
    vbl->addWidget(stopPb);
    vbl->addWidget(delaySlider);

    auto* hbl = new QHBoxLayout(frame);
    hbl->addWidget(pi);
    hbl->addLayout(vbl);

    pi->setAnimationDelay(1);

    mw->setCentralWidget(frame);

    mw->show();

    return QApplication::exec();
}
