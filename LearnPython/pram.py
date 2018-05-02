class StrEx:
    def __init__(self):
        pass
    def str2int(self, s):
        def fn(x, y):
            return x * 10 + y
        def getDic(x, y):
            return get_iter(x, y, {})
        def get_iter(x, y, dic):
            if x > y:
                return dic
            dic[str(x)] = x
            return get_iter(x+1, y, dic)
        def char2int(x):
            return get_iter(0, 9, {})[x]
        return reduce(fn, map(char2int, s))
print StrEx().str2int('0134')