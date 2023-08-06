

#ifndef SBK_UNIVERSE_PYTHON_H
#define SBK_UNIVERSE_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Bound library includes
#include <icecream.h>
#include <truck.h>
// Conversion Includes - Primitive Types

// Conversion Includes - Container Types
#include <list>
#include <map>
#include <utility>
#include <unordered_map>
#include <vector>

// Type indices
enum : int {
    SBK_ICECREAM_IDX                                         = 0,
    SBK_TRUCK_IDX                                            = 1,
    SBK_universe_IDX_COUNT                                   = 2
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkuniverseTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkuniverseModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkuniverseTypeConverters;

// Converter indices
enum : int {
    SBK_universe_CONVERTERS_IDX_COUNT                        = 1
};
// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::Icecream >() { return reinterpret_cast<PyTypeObject *>(SbkuniverseTypes[SBK_ICECREAM_IDX]); }
template<> inline PyTypeObject *SbkType< ::Truck >() { return reinterpret_cast<PyTypeObject *>(SbkuniverseTypes[SBK_TRUCK_IDX]); }

} // namespace Shiboken

#endif // SBK_UNIVERSE_PYTHON_H

