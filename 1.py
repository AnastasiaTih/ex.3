print('Здравствуйте!')
a = str(input('Введите имя: '))
b = str(input('Введите фамилию: '))
c = int(input('Введите год рождения: '))
print()
d = a + '_' + b + '_' + str(c)
print(d)
a, b = b, a
n = c + 60
print()
k = a + '_' + b + '_' + str(n)
print(k)