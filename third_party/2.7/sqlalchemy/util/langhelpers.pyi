# Stubs for sqlalchemy.util.langhelpers (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from . import compat

def md5_hex(x): ...

class safe_reraise:
    def __enter__(self): ...
    def __exit__(self, type_, value, traceback): ...

def decode_slice(slc): ...
def map_bits(fn, n): ...
def decorator(target): ...
def public_factory(target, location): ...

class PluginLoader:
    group = ... # type: Any
    impls = ... # type: Any
    auto_fn = ... # type: Any
    def __init__(self, group, auto_fn=...) -> None: ...
    def load(self, name): ...
    def register(self, name, modulepath, objname): ...

def get_cls_kwargs(cls, _set=...): ...
def inspect_func_args(fn): ...
def get_func_kwargs(func): ...
def get_callable_argspec(fn, no_self=..., _is_init=...): ...
def format_argspec_plus(fn, grouped=...): ...
def format_argspec_init(method, grouped=...): ...
def getargspec_init(method): ...
def unbound_method_to_callable(func_or_cls): ...
def generic_repr(obj, additional_kw=..., to_inspect=..., omit_kwarg=...): ...

class portable_instancemethod:
    target = ... # type: Any
    name = ... # type: Any
    def __init__(self, meth) -> None: ...
    def __call__(self, *arg, **kw): ...

def class_hierarchy(cls): ...
def iterate_attributes(cls): ...
def monkeypatch_proxied_specials(into_cls, from_cls, skip=..., only=..., name=..., from_instance=...): ...
def methods_equivalent(meth1, meth2): ...
def as_interface(obj, cls=..., methods=..., required=...): ...

class memoized_property:
    fget = ... # type: Any
    __doc__ = ... # type: Any
    __name__ = ... # type: Any
    def __init__(self, fget, doc=...) -> None: ...
    def __get__(self, obj, cls): ...
    @classmethod
    def reset(cls, obj, name): ...

def memoized_instancemethod(fn): ...

class group_expirable_memoized_property:
    attributes = ... # type: Any
    def __init__(self, attributes=...) -> None: ...
    def expire_instance(self, instance): ...
    def __call__(self, fn): ...
    def method(self, fn): ...

class MemoizedSlots:
    def __getattr__(self, key): ...

def dependency_for(modulename): ...

class dependencies:
    import_deps = ... # type: Any
    def __init__(self, *deps) -> None: ...
    def __call__(self, fn): ...
    @classmethod
    def resolve_all(cls, path): ...
    class _importlater:
        def __new__(cls, path, addtl): ...
        def __init__(self, path, addtl) -> None: ...
        def module(self): ...
        def __getattr__(self, key): ...

def asbool(obj): ...
def bool_or_str(*text): ...
def asint(value): ...
def coerce_kw_type(kw, key, type_, flexi_bool=...): ...
def constructor_copy(obj, cls, *args, **kw): ...
def counter(): ...
def duck_type_collection(specimen, default=...): ...
def assert_arg_type(arg, argtype, name): ...
def dictlike_iteritems(dictlike): ...

class classproperty:
    __doc__ = ... # type: Any
    def __init__(self, fget, *arg, **kw) -> None: ...
    def __get__(desc, self, cls): ...

class hybridproperty:
    func = ... # type: Any
    def __init__(self, func) -> None: ...
    def __get__(self, instance, owner): ...

class hybridmethod:
    func = ... # type: Any
    def __init__(self, func) -> None: ...
    def __get__(self, instance, owner): ...

class _symbol(int):
    def __new__(self, name, doc=..., canonical=...): ...
    def __reduce__(self): ...

class symbol:
    symbols = ... # type: Any
    def __new__(cls, name, doc=..., canonical=...): ...

def set_creation_order(instance): ...
def warn_exception(func, *args, **kwargs): ...
def ellipses_string(value, len_=...): ...

class _hash_limit_string(compat.text_type):
    def __new__(cls, value, num, args): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def warn(msg): ...
def warn_limited(msg, args): ...
def only_once(fn): ...
def chop_traceback(tb, exclude_prefix=..., exclude_suffix=...): ...

NoneType = ... # type: Any

def attrsetter(attrname): ...

class EnsureKWArgType(type):
    def __init__(cls, clsname, bases, clsdict) -> None: ...
