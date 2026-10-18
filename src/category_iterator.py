from src.category import Category
from src.product import Product


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self.__products = getattr(category, "_Category__products")
        self.__index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        raise StopIteration
