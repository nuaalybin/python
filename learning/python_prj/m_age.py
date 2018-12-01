
' a test module '

__author__ = 'Michael Liao'

def _private_1(name):
    return '%s is Adults' % name

def _private_2(name):
    return 'Hi, %s is Minors' % name

def greeting(name, age):
    if age > 18:
        return _private_1(name)
    else:
        return _private_2(name)