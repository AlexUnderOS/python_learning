#A lambda function can take any number of arguments, but can only have one expression.
def test():
    return 100

a = lambda : 100

print(test(),"==",a())
#
#
def test1(x, y):
    return x+y

b = lambda x, y: x+y

print(b(1,2),"==",test1(2,3))
#
#
print((lambda x, y: x+y)(1,2)) #a(1,2) == (...)(1,2)
#
#__dont use this__  just for example
def test2(x,y):
    return (lambda x,y: x+y)(x,y)

print(test2(1,2))
#
#