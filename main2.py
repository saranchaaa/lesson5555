class C1:
    pass

class C2(C1):
    pass


print(issubclass(C2, C1))