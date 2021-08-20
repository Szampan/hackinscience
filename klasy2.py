class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print("atrybut danych: MyClass.i: ", MyClass.i)
print("metoda: MyClass.f: ", MyClass.f(1)) #coś nie tak z argumentem...)
print(MyClass.__doc__)


y = MyClass()
print(y.f())

print("#######################")
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# x.f jest obiektem metody, a MyClass.f jest obiektem funkcji.
# 

x.counter = 1

while x.counter < 10:
    print(x.counter)
    x.counter *= 2

print(x.counter)
del x.counter

try:
    print(x.counter)
except:
    print("nie ma już atrybutu x.counter")