from datetime import datetime

class Transport:
    """ Базовый класс транспорт."""

    def __init__(self, brand: str, year: int) -> None:
        """
        :param brand: Бренд транспортного средства
        :param year: Год выпуска транспортного средства
        """
        self._brand = brand #Атрибут бренд сделан непубличным, так как предполагается что транспортные средства будут одного бренда
        self.year = year

    @property
    def brand(self):
        return self._brand

    def transport_age(self) -> int:
        """
        Метод, который вычисляет возраст транспортного средства
        """
        return datetime.now().year - self.year

    def service_maintenance(self) -> str:
        """
        Метод, который проверяет транспорт на право сервисного
        обслуживания в зависимости от года выпуска
        """
        return f"Транспорт {self._brand} с годом выпуска {self.year} имеет право на сервисное обслуживание"

    def __str__(self) -> str:
        return f"Бренд {self._brand}. Год выпуска {self.year}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, year={self.year!r})"

class Car(Transport):
    """Дочерний класс для автомобиля."""

    def __init__(self, brand: str, year: int, max_speed: int) -> None:
        """
        :param max_speed: Максимальная скорость автомобиля
        """
        super().__init__(brand, year)
        self.max_speed = max_speed

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed: int) -> None:
        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть больше 0")
        self._max_speed = max_speed

    def service_maintenance(self) -> str:
        return f"Автомобиль {self._brand} с годом выпуска {self.year} имеет право на сервисное обслуживание"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, year={self.year!r}, max_speed={self.max_speed!r})"

class Cycle(Transport):
    """Дочерний класс для велосипеда."""

    def __init__(self, brand: str, year: int, wheel: int) -> None:
        """
        :param wheel: Количество колёс у велосипеда
        """
        super().__init__(brand, year)
        self.wheel = wheel

    def service_maintenance(self) -> str:
        return f"Велосипед {self._brand} с годом выпуска {self.year} имеет право на сервисное обслуживание"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, year={self.year!r}, wheel={self.wheel!r})"

if __name__ == "__main__":
    car = Car("BMW", 2001, 110)
    print(car.transport_age())
    pass