from src.product import Product


class Category:
    """Категория товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        for product in products or []:
            self.add_product(product)
        Category.category_count += 1

    def add_product(self, product):
        """Добавляет товар или наследника Product, иначе TypeError."""
        if not isinstance(product, Product):
            raise TypeError(
                "Добавлять можно только объекты Product и его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "".join(f"{product}\n" for product in self.__products)

    def average_price(self) -> float:
        """Средний ценник всех товаров; 0, если категория пуста."""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."
