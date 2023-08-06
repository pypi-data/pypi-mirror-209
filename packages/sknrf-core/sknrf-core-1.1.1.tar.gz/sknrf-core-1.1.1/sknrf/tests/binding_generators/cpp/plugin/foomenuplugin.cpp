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

#include "foomenuplugin.h"
#include "../../src/fooclass.h"
#include <QtPlugin>

FooMenuPlugin::FooMenuPlugin(QObject *parent)
: QObject(parent)
{
    initialized = false;
}

void FooMenuPlugin::initialize(QDesignerFormEditorInterface * /* core */)
{
    if (initialized)
        return;
    
    initialized = true;
}

bool FooMenuPlugin::isInitialized() const
{
    return initialized;
}

QWidget *FooMenuPlugin::createWidget(QWidget *parent)
{
    return new FooMenu(parent);
}

QString FooMenuPlugin::name() const
{
    return "FooMenu";
}

QString FooMenuPlugin::group() const
{
    return "nimimo";
}

QIcon FooMenuPlugin::icon() const
{
    return QIcon();
}

QString FooMenuPlugin::toolTip() const
{
    return "";
}

QString FooMenuPlugin::whatsThis() const
{
    return "";
}

bool FooMenuPlugin::isContainer() const
{
    return false;
}

QString FooMenuPlugin::domXml() const
{
    return "<ui language=\"c++\">\n"
    " <widget class=\"FooMenu\" name=\"fooMenu\">\n"
    "  <property name=\"toolTip\" >\n"
    "   <string>Foo Menu</string>\n"
    "  </property>\n"
    "  <property name=\"whatsThis\" >\n"
    "   <string>A Sample Widget for Unit Testing</string>\n"
    "  </property>\n"
    " </widget>\n"
    "</ui>\n";
}

QString FooMenuPlugin::includeFile() const
{
    return "fooclass.h";
}

Q_EXPORT_PLUGIN2(foomenuplugin, FooMenuPlugin)
