from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


def test_category_iterator() -> None:
    p1 = Product("iPhone 15", "512GB", 210000.0, 8)
    p2 = Product("Samsung", "256GB", 180000.0, 5)
    category = Category("Смартфоны", "...", [p1, p2])

    products = list(CategoryIterator(category))

    assert products == [p1, p2]
    assert products[0].name == "iPhone 15"
