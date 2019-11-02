print("volux/core.py")

class VoluxModule:
    """Provides common metadata for every Volux module. All modules (including core) are a subclass of VoluxModule"""
    def __init__(self,name):
        self.module_name = name

class VoluxCore(VoluxModule):
    def __init__(self,*args,**kwargs):
        pass

    def add_module(self,module):
        print("print module",module)
        print("dir of module",dir(module))
        print("class",module.__class__)
        print("delattr",module.__delattr__)
        print("dict",module.__dict__)
        print("dir",module.__dir__)
        print("doc",module.__doc__)
        print("eq",module.__eq__)
        print("format",module.__format__)
        print("ge",module.__ge__)
        print("getattribute",module.__getattribute__)
        print("gt",module.__gt__)
        print("hash",module.__hash__)
        print("init",module.__init__)
        print("init_subclass",module.__init_subclass__)
        print("le",module.__le__)
        print("lt",module.__lt__)
        print("module",module.__module__)
        print("ne",module.__ne__)
        print("new",module.__new__)
        print("reduce",module.__reduce__)
        print("reduce_ex",module.__reduce_ex__)
        print("repr",module.__repr__)
        print("setattr",module.__setattr__)
        print("sizeof",module.__sizeof__)
        print("str",module.__str__)
        print("subclasshook",module.__subclasshook__)
        print("weakref",module.__weakref__)
