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
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_counts(product: Product) -> None:
    Category("Смартфоны", "...", [product])
    Category("Телевизоры", "...", [product, product])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_add_product(product: Product) -> None:
    category = Category("Смартфоны", "...", [])
    category.add_product(product)
    assert Category.product_count == 1
    assert "iPhone 15" in category.products


def test_products_getter(product: Product) -> None:
    category = Category("Смартфоны", "...", [product])
    assert category.products == (
        "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_new_product() -> None:
    data = {
        "name": "Samsung",
        "description": "256GB",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Samsung"
    assert product.price == 180000.0


def test_price_setter_positive(product: Product) -> None:
    product.price = 100000.0
    assert product.price == 100000.0


def test_price_setter_negative(
    product: Product, capsys: pytest.CaptureFixture[str]
) -> None:
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть" in captured.out
    assert product.price == 210000.0
