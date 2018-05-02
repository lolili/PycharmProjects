import sys
def f():
    '''This is a func.

    hello.'''
    global i
    i=2
f()
print f.__doc__

print sys.executable
