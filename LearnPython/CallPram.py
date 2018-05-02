# from pram import StrEx
# s = StrEx()
# print str2int('0424')


# def calc(*nums):
#     sum = 0
#     print nums
#     for i in nums:
#         sum = sum + i
#     return sum
# nums = [1, 2, 3]
# print calc(*nums)

####################  return func  #################
# def f():
#     i = 1
#     fs = []
#     for i in range(1,4):
#         def g(j):
#             def ff():
#                 return j+2
#             return ff
#         fs.append(g(i))
#     i = -1
#     return fs
# for i in range(0,3):
#     print f()[i]()

'''decorator'''
def call_log(text):
    def log(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print text
                print "call %s():" % func.__name__
                return func(*args, **kw)
            return wrapper
        return decorator
    text += '...'
    return log(text)
@call_log('Executing')
def now_date():
    print "2013-01-13"

now_date()

