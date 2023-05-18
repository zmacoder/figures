
default_radius = 5
radius = int(input('Введите радиус: '))
def circle_perimetr():
    if radius > 0:
        print(2 * 3.14 * radius)
    else:
        print(2 * 3.14 * default_radius)
circle_perimetr()

def circle_area():
    if radius > 0:
        print(3.14 * (radius**2))
    else:
        print(3.14 * (default_radius**2))
circle_area()