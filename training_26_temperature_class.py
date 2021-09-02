class Kelvin:
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None):
        return self.value
    def __set__(self, obj, temp):
        self.value = float(temp)

class Celsius:
    def __get__(self, obj, type=None):
        return float(obj.kelvin) - 273.15
    def __set__(self, obj, temp):
        obj.kelvin = temp + 273.15

class Fahrenheit:
    def __get__(self, obj, type=None):
        return obj.kelvin * 9/5 - 459.67
    def __set__(self, obj, temp):
        obj.kelvin = (temp + 459.67) * 5/9

class Temperature:
    kelvin = Kelvin()
    celsius = Celsius()
    fahrenheit = Fahrenheit()


t1 = Temperature()
t1.celsius = 0
print(t1.kelvin)
print(t1.celsius)
print(t1.fahrenheit)

t1.celsius += 1
print(t1.kelvin)
print(t1.celsius)