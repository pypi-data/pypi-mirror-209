# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
import sys
if not(hasattr(sys,"frozen")):
    if sys.platform == 'win32':
        import site, os
        trk_path = site.getsitepackages()[1]+"\\polhemusFT"
        os.environ["PATH"] += os.pathsep + trk_path 
        sys.path.append(trk_path)
        os.environ["PATH"] += os.pathsep + os.path.dirname(__file__)

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _polhemusFT
else:
    import _polhemusFT

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class polhemusFT(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    PositionTooltipX1 = property(_polhemusFT.polhemusFT_PositionTooltipX1_get, _polhemusFT.polhemusFT_PositionTooltipX1_set)
    PositionTooltipY1 = property(_polhemusFT.polhemusFT_PositionTooltipY1_get, _polhemusFT.polhemusFT_PositionTooltipY1_set)
    PositionTooltipZ1 = property(_polhemusFT.polhemusFT_PositionTooltipZ1_get, _polhemusFT.polhemusFT_PositionTooltipZ1_set)
    AngleX1 = property(_polhemusFT.polhemusFT_AngleX1_get, _polhemusFT.polhemusFT_AngleX1_set)
    AngleY1 = property(_polhemusFT.polhemusFT_AngleY1_get, _polhemusFT.polhemusFT_AngleY1_set)
    AngleZ1 = property(_polhemusFT.polhemusFT_AngleZ1_get, _polhemusFT.polhemusFT_AngleZ1_set)
    PositionTooltipX2 = property(_polhemusFT.polhemusFT_PositionTooltipX2_get, _polhemusFT.polhemusFT_PositionTooltipX2_set)
    PositionTooltipY2 = property(_polhemusFT.polhemusFT_PositionTooltipY2_get, _polhemusFT.polhemusFT_PositionTooltipY2_set)
    PositionTooltipZ2 = property(_polhemusFT.polhemusFT_PositionTooltipZ2_get, _polhemusFT.polhemusFT_PositionTooltipZ2_set)
    AngleX2 = property(_polhemusFT.polhemusFT_AngleX2_get, _polhemusFT.polhemusFT_AngleX2_set)
    AngleY2 = property(_polhemusFT.polhemusFT_AngleY2_get, _polhemusFT.polhemusFT_AngleY2_set)
    AngleZ2 = property(_polhemusFT.polhemusFT_AngleZ2_get, _polhemusFT.polhemusFT_AngleZ2_set)
    PositionTooltipX3 = property(_polhemusFT.polhemusFT_PositionTooltipX3_get, _polhemusFT.polhemusFT_PositionTooltipX3_set)
    PositionTooltipY3 = property(_polhemusFT.polhemusFT_PositionTooltipY3_get, _polhemusFT.polhemusFT_PositionTooltipY3_set)
    PositionTooltipZ3 = property(_polhemusFT.polhemusFT_PositionTooltipZ3_get, _polhemusFT.polhemusFT_PositionTooltipZ3_set)
    AngleX3 = property(_polhemusFT.polhemusFT_AngleX3_get, _polhemusFT.polhemusFT_AngleX3_set)
    AngleY3 = property(_polhemusFT.polhemusFT_AngleY3_get, _polhemusFT.polhemusFT_AngleY3_set)
    AngleZ3 = property(_polhemusFT.polhemusFT_AngleZ3_get, _polhemusFT.polhemusFT_AngleZ3_set)
    PositionTooltipX4 = property(_polhemusFT.polhemusFT_PositionTooltipX4_get, _polhemusFT.polhemusFT_PositionTooltipX4_set)
    PositionTooltipY4 = property(_polhemusFT.polhemusFT_PositionTooltipY4_get, _polhemusFT.polhemusFT_PositionTooltipY4_set)
    PositionTooltipZ4 = property(_polhemusFT.polhemusFT_PositionTooltipZ4_get, _polhemusFT.polhemusFT_PositionTooltipZ4_set)
    AngleX4 = property(_polhemusFT.polhemusFT_AngleX4_get, _polhemusFT.polhemusFT_AngleX4_set)
    AngleY4 = property(_polhemusFT.polhemusFT_AngleY4_get, _polhemusFT.polhemusFT_AngleY4_set)
    AngleZ4 = property(_polhemusFT.polhemusFT_AngleZ4_get, _polhemusFT.polhemusFT_AngleZ4_set)
    StylusButton = property(_polhemusFT.polhemusFT_StylusButton_get, _polhemusFT.polhemusFT_StylusButton_set)

    def Initialize(self) -> "bool":
        return _polhemusFT.polhemusFT_Initialize(self)

    def Close(self) -> "void":
        return _polhemusFT.polhemusFT_Close(self)

    def Run(self) -> "int":
        return _polhemusFT.polhemusFT_Run(self)

    def __init__(self):
        _polhemusFT.polhemusFT_swiginit(self, _polhemusFT.new_polhemusFT())
    __swig_destroy__ = _polhemusFT.delete_polhemusFT

# Register polhemusFT in _polhemusFT:
_polhemusFT.polhemusFT_swigregister(polhemusFT)


def new_intp() -> "int *":
    return _polhemusFT.new_intp()

def copy_intp(value: "int") -> "int *":
    return _polhemusFT.copy_intp(value)

def delete_intp(obj: "int *") -> "void":
    return _polhemusFT.delete_intp(obj)

def intp_assign(obj: "int *", value: "int") -> "void":
    return _polhemusFT.intp_assign(obj, value)

def intp_value(obj: "int *") -> "int":
    return _polhemusFT.intp_value(obj)

def new_floatp() -> "float *":
    return _polhemusFT.new_floatp()

def copy_floatp(value: "float") -> "float *":
    return _polhemusFT.copy_floatp(value)

def delete_floatp(obj: "float *") -> "void":
    return _polhemusFT.delete_floatp(obj)

def floatp_assign(obj: "float *", value: "float") -> "void":
    return _polhemusFT.floatp_assign(obj, value)

def floatp_value(obj: "float *") -> "float":
    return _polhemusFT.floatp_value(obj)

def new_doublep() -> "double *":
    return _polhemusFT.new_doublep()

def copy_doublep(value: "double") -> "double *":
    return _polhemusFT.copy_doublep(value)

def delete_doublep(obj: "double *") -> "void":
    return _polhemusFT.delete_doublep(obj)

def doublep_assign(obj: "double *", value: "double") -> "void":
    return _polhemusFT.doublep_assign(obj, value)

def doublep_value(obj: "double *") -> "double":
    return _polhemusFT.doublep_value(obj)

def new_boolp() -> "bool *":
    return _polhemusFT.new_boolp()

def copy_boolp(value: "bool") -> "bool *":
    return _polhemusFT.copy_boolp(value)

def delete_boolp(obj: "bool *") -> "void":
    return _polhemusFT.delete_boolp(obj)

def boolp_assign(obj: "bool *", value: "bool") -> "void":
    return _polhemusFT.boolp_assign(obj, value)

def boolp_value(obj: "bool *") -> "bool":
    return _polhemusFT.boolp_value(obj)


