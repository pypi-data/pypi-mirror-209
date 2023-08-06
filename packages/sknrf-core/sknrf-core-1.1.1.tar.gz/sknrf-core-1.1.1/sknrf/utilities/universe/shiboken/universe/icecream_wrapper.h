#ifndef SBK_ICECREAMWRAPPER_H
#define SBK_ICECREAMWRAPPER_H

#include <icecream.h>


// Argument includes
#include <icecream.h>
class IcecreamWrapper : public Icecream
{
public:
    IcecreamWrapper(const std::string & flavor);
    Icecream * clone() override;
    const std::string getFlavor() override;
    ~IcecreamWrapper();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[2];
};

#endif // SBK_ICECREAMWRAPPER_H

