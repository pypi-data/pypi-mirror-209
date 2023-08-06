#ifndef QPROGRESSINDICATORPLUGIN_H
#define QPROGRESSINDICATORPLUGIN_H

#include <QtUiPlugin/QDesignerCustomWidgetInterface>
#include "sknrfconfig.h"

class QProgressIndicatorPlugin : public QObject, public QDesignerCustomWidgetInterface
{
    Q_OBJECT
    Q_INTERFACES(QDesignerCustomWidgetInterface)
#if QT_VERSION >= 0x050000
    Q_PLUGIN_METADATA(IID "org.qt-project.Qt.QDesignerCustomWidgetInterface")
#endif // QT_VERSION >= 0x050000
    
public:
    explicit QProgressIndicatorPlugin(QObject *parent = nullptr);
    
    [[nodiscard]] bool isContainer() const override;
    [[nodiscard]] bool isInitialized() const override;
    [[nodiscard]] QIcon icon() const override;
    [[nodiscard]] QString domXml() const override;
    [[nodiscard]] QString group() const override;
    [[nodiscard]] QString includeFile() const override;
    [[nodiscard]] QString name() const override;
    [[nodiscard]] QString toolTip() const override;
    [[nodiscard]] QString whatsThis() const override;
    QWidget *createWidget(QWidget *parent) override;
    void initialize(QDesignerFormEditorInterface *core) override;
    
private:
    bool m_initialized;
};

#endif
