/****************************************************************************
 **
 ** Copyright (C) 2014 Digia Plc and/or its subsidiary(-ies).
 ** Contact: http://www.qt-project.org/legal
 **
 ** This file is part of the examples of the Qt Toolkit.
 **
 ** $QT_BEGIN_LICENSE:BSD$
 ** You may use this file under the terms of the BSD license as follows:
 **
 ** "Redistribution and use in source and binary forms, with or without
 ** modification, are permitted provided that the following conditions are
 ** met:
 **   * Redistributions of source code must retain the above copyright
 **     notice, this list of conditions and the following disclaimer.
 **   * Redistributions in binary form must reproduce the above copyright
 **     notice, this list of conditions and the following disclaimer in
 **     the documentation and/or other materials provided with the
 **     distribution.
 **   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
 **     of its contributors may be used to endorse or promote products derived
 **     from this software without specific prior written permission.
 **
 **
 ** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 ** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 ** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 ** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 ** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 ** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 ** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 ** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 ** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 ** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 ** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
 **
 ** $QT_END_LICENSE$
 **
 ****************************************************************************/

#include "qttreepropertybrowserplugin.h"
#include "qttreepropertybrowser.h"
#include <QtPlugin>

QtTreePropertyBrowserPlugin::QtTreePropertyBrowserPlugin(QObject *parent)
: QObject(parent)
{
    m_initialized = false;
}

void QtTreePropertyBrowserPlugin::initialize(QDesignerFormEditorInterface * /* core */)
{
    if (m_initialized)
        return;
    
    m_initialized = true;
}

bool QtTreePropertyBrowserPlugin::isInitialized() const
{
    return m_initialized;
}

QWidget *QtTreePropertyBrowserPlugin::createWidget(QWidget *parent)
{
    return new QtTreePropertyBrowser(parent);
}

QString QtTreePropertyBrowserPlugin::name() const
{
    return "QtTreePropertyBrowser";
}

QString QtTreePropertyBrowserPlugin::group() const
{
    return "Scikit Nonlinear";
}

QIcon QtTreePropertyBrowserPlugin::icon() const
{
    return QIcon();
}

QString QtTreePropertyBrowserPlugin::toolTip() const
{
    return QLatin1String("");
}

QString QtTreePropertyBrowserPlugin::whatsThis() const
{
    return QLatin1String("");
}

BrowserCol QtTreePropertyBrowserPlugin::attribute1() const
{
    return BrowserCol::NONE;
}

BrowserCol QtTreePropertyBrowserPlugin::attribute2() const
{
    return BrowserCol::NONE;
}

BrowserCol QtTreePropertyBrowserPlugin::attribute3() const
{
    return BrowserCol::NONE;
}

bool QtTreePropertyBrowserPlugin::isContainer() const
{
    return false;
}

QString QtTreePropertyBrowserPlugin::domXml() const
{
    return "<ui language=\"c++\">\n"
    " <widget class=\"QtTreePropertyBrowser\" name=\"treePropertyBrowser\">\n"
    "  <property name=\"geometry\">\n"
    "   <rect>\n"
    "    <x>0</x>\n"
    "    <y>0</y>\n"
    "    <width>100</width>\n"
    "    <height>100</height>\n"
    "   </rect>\n"
    "  </property>\n"
    "  <property name=\"toolTip\" >\n"
    "   <string>Property Browser</string>\n"
    "  </property>\n"
    "  <property name=\"whatsThis\" >\n"
    "   <string>The Property Browser Controls Table Properties</string>\n"
    "  </property>\n"
    " </widget>\n"
    "</ui>\n";
}

QString QtTreePropertyBrowserPlugin::includeFile() const
{
    return "propertybrowser.h";
}

#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(qtpropertytableplugin, QtTreePropertyBrowserPlugin)
#endif // QT_VERSION < 0x050000
