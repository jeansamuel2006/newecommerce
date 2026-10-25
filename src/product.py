from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __add__(self, other: object) -> float:
        ...


class CreationLoggerMixin:
    """Печатает в консоль, какой объект и с какими параметрами создан."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.name!r}, "
            f"{self.description!r}, {self.price!r}, {self.quantity!r})"
        )


class Product(CreationLoggerMixin, BaseProduct):
    """Базовый класс товара."""

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, data):
        """Создает товар из словаря."""
        return cls(**data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Складывать можно только товары строго одного класса
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Смартфон."""

    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Трава газонная."""

    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
