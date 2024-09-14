class Vehicle:
    _COLOR_VARIANTS = ['Белый', 'Черный', 'Мокрый асфальт', 'Лазурь']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = ''
        for default_color in self._COLOR_VARIANTS:
            if color.lower() == default_color.lower():
                self.__color = color
        if not self.__color:
            self.__color = self._COLOR_VARIANTS[0]
            print(f'Невозможно создать объект с цветом {color}. '
                  f'Объект создан с цветом по умолчанию ({self._COLOR_VARIANTS[0]})')

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        for default_color in self._COLOR_VARIANTS:
            if new_color.lower() == default_color.lower():
                self.__color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('Черный')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()



