import doctest

class Vk:
    def __init__(self, friends: int, messages: int):
        """
        Создание и подготовка к работе объекта "Vk"

        :param friends: Количество друзей
        :param messages: Количество сообщений
        Пример:
        >>> vk = Vk(70, 100)  # инициализация экземпляра класса
        """
        if not isinstance(friends, int):
            raise TypeError("Количество друзей должно быть типа int")
        if friends < 0:
            raise ValueError("Количество друзей положительным числом или равно 0")
        self.friends = friends

        if not isinstance(messages, int):
            raise TypeError("Количество сообщений должно быть типа int")
        if messages < 0:
            raise ValueError("Количество сообщений положительным числом или равно 0")
        self.messages = messages

    def no_friends(self) -> bool:
        """
        Функция которая проверяет есть ли у пользователя друзья

        :return: У пользователя нет друзей
        Примеры:
        >>> vk = Vk(70, 100)
        >>> vk.no_friends()
        """
        ...

    def add_friends(self, friend: int) -> None:
        """
        Добавление новых друзей

        :param friend: Количество новых друзей

        :raise ValueError: Если количество новых друзей меньше 0
        Примеры:
        >>> vk = Vk(70, 100)
        >>> vk.add_friends(2)
        """
        if not isinstance(friend, int):
            raise TypeError("Количество новых друзей должно быть типа int")
        if friend < 0:
            raise ValueError("Количество новых друзей должно быть положительным числом или равно 0")
        ...

    def delete_message(self, message: int) -> None:
        """
        Удаление сообщений

        :param message: Количество удаляемых сообщений

        :raise ValueError: Если количество удаляемых сообщений отрицательное число или меньше 0
        Примеры:
        >>> vk = Vk(70, 100)
        >>> vk.delete_message(10)
        """
        ...

class App:
    def __init__(self, name: str, app_version: float, grades: int):
        """
        Создание и подготовка к работе объекта "App"

        :param name: Название мобильного приложения
        :param app_version: Версия мобильного приложения
        :param grades: Оценка приложения
        Пример:
        >>> app = App("Telegram", 1.0, 5)
        """
        if not isinstance(name, str):
            raise TypeError("Название приложения должно быть типа str")
        if not name:
            raise ValueError("Название приложения не может отсутствовать")
        self.name = name

        if not isinstance(app_version, float):
            raise TypeError("Версия приложения должна быть типа float")
        if app_version < 1.0:
            raise ValueError("Версия приложения должна быть больше либо равна 1.0")
        self.app_version = app_version

        if not isinstance(grades, int):
            raise TypeError("Оценка приложения должна быть типа int")
        if not 1 <= grades <= 5:
            raise ValueError("Оценка приложения лежит в диапазоне от 1 до 5")
        self.grades = grades

    def update(self, version: float) -> None:
        """
        Обновление версии приложения
        
        :param version: Новая версия приложения

        :raise ValueError: Если новая версия совпадает с текущей
        Примеры:
        >>> app = App("Telegram", 1.0, 5)
        >>> app.update(1.1)
        """
        if not isinstance(version, float):
            raise TypeError("Новая версия приложения должна быть типа float")
        ...

    def new_grade(self, grade: int) -> None:
        """
        Изменение оценки приложения

        :param grade: новая оценка приложения

        :raise ValueError: Если новая оценка не лежит в диапазоне от 0 до 5
        Примеры:
        >>> app = App("Telegram", 1.0, 5)
        >>> app.new_grade(3)
        """
        ...

class Laptop:
    def __init__(self, name: str, charge_level: int):
        """
        Создание и подготовка к работе объекта "Laptop"

        :param name: Название модели ноутбука
        :param charge_level: Уровень заряда ноутбука
        Пример:
        >>> laptop = Laptop("Macbook air", 91)
        """

        if not isinstance(name, str):
            raise TypeError("Название модели ноутбука должно быть типа str")
        if not name:
            raise ValueError("Название модели не может отсутствовать")
        self.name = name

        if not isinstance(charge_level, int):
            raise TypeError("Уровень заряда должен быть типа int")
        if charge_level < 0:
            raise ValueError("Уровень заряда должен быть больше либо равен 0")
        self.charge_level = charge_level

    def recharge(self, charge: int) -> None:
        """
        Повышение заряда аккумулятора

        :param charge: На сколько повышвется уровень заряда

        :raise ValueError: Уровень заряда должен лежать в диапазоне от 0 до 100
        Примеры:
        >>> laptop = Laptop("Macbook air", 91)
        >>> laptop.recharge(2)
        """
        if not isinstance(charge, int):
            raise ValueError("Уровень заряда должен быть типа int")
        ...

    def discharge(self, charge_: int) -> None:
        """
        Снижение уровня заряда

        :param charge_: На сколько снижается уровень заряда

        :raise ValueError: Если снижаемый уровень заряда превышает допустимые 100
        Примеры:
        >>> laptop = Laptop("Macbook air", 91)
        >>> laptop.discharge(10)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    
