class Reactangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def give_me_info(self):
        print (f"Высота: {self.height}\n" +
               f'Ширина: {self.width}')
    def give_me_square (self):
        square = self.width * self.height
        print (f"Площадь прямоугольника: {square}")
    def give_me_perimeter (self):
        perimetr = 2 * (self.width + self.height)
        print (f"Периметр прямоугольника: {perimetr}")
        return perimetr
new_reactangle = Reactangle (2,4)
new_reactangle.give_me_info()
new_reactangle.give_me_square()
new_reactangle.give_me_perimeter()