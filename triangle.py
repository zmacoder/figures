
a = 7
b = 2
c = 8
d = 13


a = int(input('''Введитке соотношение сторон:
a = '''))
b = int(input("b = "))
c = int(input("c = "))

def triangle_perimetr():
    if a > 0:
        if b > 0:
            if c > 0:
                perimetr = a + b + c
                print("Периметр треуголтника = ", perimetr)
triangle_perimetr()

def triangle_area():
