#include <QtPlugin>
#include <qprogressindicator.h>
#include "qprogressindicatorplugin.h"

QProgressIndicatorPlugin::QProgressIndicatorPlugin(QObject *parent)
    : QObject(parent)
{
    m_initialized = false;
}

void QProgressIndicatorPlugin::initialize(QDesignerFormEditorInterface * /* core */)
{
    if (m_initialized)
        return;
    
    m_initialized = true;
}

bool QProgressIndicatorPlugin::isInitialized() const
{
    return m_initialized;
}

QWidget *QProgressIndicatorPlugin::createWidget(QWidget *parent)
{
    auto* pi = new QProgressIndicator(parent);
    pi->startAnimation();
    return pi;
}

QString QProgressIndicatorPlugin::name() const
{
    return "QProgressIndicator";
}

QString QProgressIndicatorPlugin::group() const
{
    return "Scikit Nonlinear";
}

QIcon QProgressIndicatorPlugin::icon() const
{
    return {};
}

QString QProgressIndicatorPlugin::toolTip() const
{
    return QLatin1String("");
}

QString QProgressIndicatorPlugin::whatsThis() const
{
    return QLatin1String("");
}

bool QProgressIndicatorPlugin::isContainer() const
{
    return false;
}

QString QProgressIndicatorPlugin::domXml() const
{
    return "<ui language=\"c++\">\n"
    " <widget class=\"QProgressIndicator\" name=\"qProgressIndicator\">\n"
    "  <property name=\"toolTip\" >\n"
    "   <string>Progress Indicator</string>\n"
    "  </property>\n"
    "  <property name=\"whatsThis\" >\n"
    "   <string>The Progress Indicator indicates the system is busy</string>\n"
    "  </property>\n"
    " </widget>\n"
    "</ui>\n";
}

QString QProgressIndicatorPlugin::includeFile() const
{
    return QLatin1String("qprogressindicator.h");
}

#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(qprogressindicatorplugin, QProgressIndicatorPlugin)
#endif // QT_VERSION < 0x050000

