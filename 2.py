print('Введите длины катетов треугольника')
a = float(input('a='))
b = float(input('b='))
c = (a**2 + b**2)**0.5
p = a + b + c
s = 0.5*a*b
print('периметр:', str(p) + ';', 'площадь:', s)

