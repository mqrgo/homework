from datetime import datetime
from time import sleep


# 1. Создать класс для геометрической фигуры на выбор и добавить в него два метода
# – первый для расчета площади, второй для расчета периметра
class Square:
    """
    Геометрическая фигура - квадрат.
    Сторона валидируется с помощью сеттера (на всякий случай)
    """

    def __init__(self, size: int | float):
        self.side = size

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value: int | float):
        if not isinstance(value, (int, float)):
            raise ValueError('Size should be int or float')
        self._side = value

    def perimeter(self) -> int | float:
        return 4 * self.side

    def area(self) -> int | float:
        return self.side * self.side


# sq = Square(12)
# print(sq.side)
# print(sq.perimeter())
# print(sq.area())


# 2. Создать класс “Человек” с полями: имя, город проживания и год рождения.
# Написать метод, который будет возвращать возраст человека в годах


class Person:
    """
    Возраст может быть +- неправильный т.к. мы используем только год рождения, а не полную дату.
    + добавил валидацию на год рождения через сеттер
    """

    def __init__(self, first_name: str, current_city: str, year_of_birth: int):
        self.first_name = first_name
        self.current_city = current_city
        self.year_of_birth = year_of_birth

    @property
    def year_of_birth(self):
        return self._year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, year):
        if not isinstance(year, int):
            raise ValueError('Year of birth should be int')
        self._year_of_birth = year

    def get_age(self) -> int:
        return datetime.now().year - self.year_of_birth


# pr = Person('Egor', 'Moscow', 2000)
# print(pr.get_age())


# 3. Создать класс калькулятор и описать в нём методы для базовых математических операций для двух чисел
class BasicCalc:

    @classmethod
    def plus(cls, x, y):
        return x + y

    @classmethod
    def minus(cls, x, y):
        return x - y

    @classmethod
    def multiplication(cls, x, y):
        return x * y

    @classmethod
    def division_with_remainder(cls, x, y, fractional_part=3):
        """
        В этот метод можно передать ожидаемое количество знаков после запятой
        По дефолту будет выводиться 3 знака после запятой
        """
        return round(x / y, fractional_part)

    @classmethod
    def division_without_remainder(cls, x, y):
        return x // y

    @classmethod
    def remainder_of_the_division(cls, x, y):
        return x % y


# print(BasicCalc.plus(2, 3))
# print(BasicCalc.minus(2, 3))
# print(BasicCalc.division_with_remainder(2, 3, 12))
# print(BasicCalc.division_without_remainder(2, 3))
# print(BasicCalc.remainder_of_the_division(2, 3))


# 4. Изучить метод  __str__, создать класс с данным методом, продемонстрировать его выполнение
class Car:

    def __init__(self, name: str, model: str, color: str, max_speed: int):
        self.name = name
        self.model = model.upper()
        self.color = color
        self.max_speed = max_speed

    def __str__(self) -> str:
        return f'Car name: {self.name} {self.model}.\nColor: {self.color}.\nMax speed: {self.max_speed} km/h.'


# bmw = Car('BMW', '12gt', 'blue', 123)
# print(bmw)


# 5. Создать базовый класс сотрудник и два дочерних класса – менеджер и работник. В базовый класс добавить get_paid(),
# который в дальнейшем переопределить в дочерних, чтобы сотрудники разных должностей получали различную зарплату 
'''
Условие этой задачи такое, на грани понимания. Я делал раньше похожу задачу, где зарплата каждого сотрудника считалась
в зависимости от условий. В этой сделаю так же. 
'''


class Employee:

    def __init__(self, first_name: str, last_name: str, salary: int | float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_paid(self) -> int | float:
        return self.salary

    def __str__(self) -> str:
        return f'Employee: {self.first_name} {self.last_name}.\nSalary: {self.get_paid()} rub/h.'


class Manager(Employee):
    """
    Зарплата менеджера расcчитывается следующим образом:
    оклад + процент_от_суммы_продаж_за_месяц
    """

    def __init__(self, first_name, last_name, salary, sum_of_sales, percent):
        super().__init__(first_name, last_name, salary)
        self.sum_of_sales = sum_of_sales
        self.percent = percent

    def get_paid(self):
        return self.salary + (self.sum_of_sales * self.percent / 100)

    def __str__(self):
        return f'{super().__str__()}\nPosition: Manager.'


class Worker(Employee):
    """
    Зарплата рабочего раcсчитывается следующим образом:
    оклад + цена_за_делать * кол-во_деталей
    """

    def __init__(self, first_name, last_name, salary, per_detail, details):
        super().__init__(first_name, last_name, salary)
        self.per_detail = per_detail
        self.details = details

    def get_paid(self):
        return self.salary + (self.per_detail * self.details)

    def __str__(self):
        return f'{super().__str__()}\nPosition: Worker.'


# m1 = Manager(
#     first_name='Yurii',
#     last_name='Novikov',
#     salary=12_000,
#     sum_of_sales=200_000,
#     percent=10,
# )
# print(m1, '\n')

# w1 = Worker(
#     first_name='Egor',
#     last_name='Korolev',
#     salary=8_000,
#     per_detail=103,
#     details=120,
# )
# print(w1)

# 6. * Изучить что такое множественное наследование и миксины, привести пример использования данных концепций ООП
# Множественное наследование
'''
Класс боевого робота обладает атрибутами и методами родительских классов
'''


class BasicScheme:

    def __init__(self, name: str, model: int):
        self.name = name
        self.model = model
        self.battery_percent = 100
        self.charging = False

    def __str__(self):
        return f'{self.name} {self.model}\n{self.battery_percent}\n{self.charging}'

    def status(self):
        return 'charging' if self.charging is True else 'not charging'


class Wings:

    def __init__(self, wing_size: int):
        self.wing_size = wing_size

    def fly(self):
        return 'im flying'


class WarLordRobot(BasicScheme, Wings):

    def __init__(self, name: str, model: int, wing_size: int, weapon: str):
        BasicScheme.__init__(self, name, model)
        Wings.__init__(self, wing_size)
        self.weapon = weapon

    def shoot(self):
        return f'Im shooting with {self.weapon}'


# r = WarLordRobot('YY3', '21AAD', 12, 'pistol')
# print(r)
# print(r.status())
# print(r.fly())
# print(r.shoot())

# Миксины
'''
FuncTimerMixin - логирует вызовы функции power экземпляра класса TestClass
'''


class FuncTimerMixin:
    logs = []

    def get_log(self):
        for log in FuncTimerMixin.logs:
            print(log)

    def add_log(self, log_value):
        FuncTimerMixin.logs.append(log_value)


class TestClass(FuncTimerMixin):

    def __init__(self, n: int):
        self.n = n

    def power(self):
        self.add_log(f'Function {self.power.__name__} was called at {datetime.now()}')
        return self.n ** 1000

# t = TestClass(10000)
# t1 = TestClass(20000)
# t.power()
# sleep(1)
# t.power()
# t.power()
# sleep(1)
# t1.power()
# print(FuncTimerMixin.logs)
