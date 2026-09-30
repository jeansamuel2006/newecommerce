import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product() -> Product:
    return Product("iPhone 15", "512GB", 210000.0, 8)


@pytest.fixture(autouse=True)
def reset_counts() -> None:
    Category.category_count = 0
    Category.product_count = 0


def test_product_init(product: Product) -> None:
    assert product.name == "iPhone 15"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_category_init(product: Product) -> None:
    category = Category("Смартфоны", "Описание", [product])
    assert category.name == "Смартфоны"
    assert category.products == [product]


def test_counts(product: Product) -> None:
    Category("Смартфоны", "...", [product])
    Category("Телевизоры", "...", [product, product])
    assert Category.category_count == 2
    assert Category.product_count == 3
