import inspect

def get_keyword_param_names(locs):
    func = globals()[inspect.stack()[1].__code__.co_varnames]
    print(func, type(func))
    return {name:locs[name] for name, param in inspect.signature(func).parameters.items()
        if (
            param.kind is inspect.Parameter.KEYWORD_ONLY
            or param.kind is inspect.Parameter.VAR_KEYWORD
        )}

def foo(*, a, b, **kwargs):
    return get_keyword_param_names(locals())
s = foo(a=2, b=3)
print(s)