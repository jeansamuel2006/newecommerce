import pytest

from src.category import Category
from src.product import Product


def test_zero_quantity_raises() -> None:
    """Товар с нулевым количеством вызывает ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Product("iPhone 15", "512GB", 210000.0, 0)
    assert str(exc_info.value) == (
        "Товар с нулевым количеством не может быть добавлен"
    )


def test_new_product_zero_quantity_raises() -> None:
    """new_product тоже проверяет нулевое количество."""
    data = {
        "name": "Samsung",
        "description": "256GB",
        "price": 180000.0,
        "quantity": 0,
    }
    with pytest.raises(ValueError):
        Product.new_product(data)


def test_positive_quantity_ok() -> None:
    """Ненулевое количество создаётся без ошибки."""
    product = Product("Чехол", "Силикон", 10.0, 3)
    assert product.quantity == 3


def test_average_price() -> None:
    """Средний ценник = сумма цен / число товаров."""
    p1 = Product("A", "...", 100.0, 2)
    p2 = Product("B", "...", 200.0, 5)
    p3 = Product("C", "...", 300.0, 1)
    category = Category("Тест", "Описание", [p1, p2, p3])
    assert category.average_price() == 200.0


def test_average_price_empty() -> None:
    """Пустая категория возвращает 0, без ZeroDivisionError."""
    category = Category("Пустая", "Описание")
    assert category.average_price() == 0
