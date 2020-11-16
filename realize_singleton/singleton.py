# ========1.作为模块使用========
class Marry1():
    def __init__(self):
        self.name = 'Marry'


marry = Marry1()


# ========2.使用__new__方法========
class Marry2():
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return Marry2._instance


M1 = Marry2()
M2 = Marry2()
print(id(M1))
print(id(M2))


# ========3.使用装饰器========
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class Marry3(object):
    def __init__(self, x=0):
        self.x = x


M3 = Marry3(2)
M4 = Marry3(3)
print(id(M3))
print(id(M4))


# ========4.使用元类type========
class SingletonType(type):
    def __call__(cls, *args, **kwargs):  # 这里的cls即是Marry类
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonType, self).__call__(*args,
                                                                **kwargs)  # type的__call__方法会调用Marry的__new__方法创建对象，然后调用__init__初始化对象
        return cls._instance


class Marry4(metaclass=SingletonType):  # 指定Marry的type为SingletonType
    def __init__(self):
        self.name = "marry"
        self.age = 25

    # def __call__(self, *args, **kwargs):


marry5 = Marry4()
marry6 = Marry4()
print(id(marry5))
print(id(marry6))
