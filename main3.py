import inspect as ins
import requests as rq


class C1:
    pass


def f1():
    pass


print(ins.isclass(C1))
print(ins.isfunction(f1()))
print(ins.ismodule(rq))
