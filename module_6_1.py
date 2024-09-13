class Animal:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.alive = True

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __str__(self):
        return f'{self.name}: млекопитающее'


class Predator(Animal):
    def __str__(self):
        return f'{self.name}: хищник'


class Flower(Plant):
    def __str__(self):
        return f'{self.name}: цветковое растение'


class Fruit(Plant):
    edible = True

    def __str__(self):
        return f'{self.name}: плод'


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
