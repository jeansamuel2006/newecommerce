import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def phone():
    return Smartphone("Samsung", "256GB", 100.0, 2, 95.5, "S23", 256, "Серый")


@pytest.fixture
def phone2():
    return Smartphone("Iphone", "512GB", 200.0, 3, 98.2, "15", 512, "Синий")


@pytest.fixture
def grass():
    return LawnGrass(
        "Трава", "Элитная", 50.0, 10, "Россия", "7 дней", "Зеленый"
    )


@pytest.fixture
def product():
    return Product("Чехол", "Силикон", 10.0, 5)


def test_smartphone_init(phone):
    assert isinstance(phone, Product)
    assert phone.efficiency == 95.5
    assert phone.model == "S23"
    assert phone.memory == 256
    assert phone.color == "Серый"
    assert phone.price == 100.0


def test_lawn_grass_init(grass):
    assert isinstance(grass, Product)
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_product_str(product):
    assert str(product) == "Чехол, 10.0 руб. Остаток: 5 шт."


def test_new_product():
    item = Product.new_product(
        {"name": "A", "description": "B", "price": 1.0, "quantity": 2}
    )
    assert item.name == "A"


def test_price_setter(product, capsys):
    product.price = 20.0
    assert product.price == 20.0
    product.price = -5
    assert product.price == 20.0
    assert "некорректная" in capsys.readouterr().out


def test_add_same_class(phone, phone2):
    assert phone + phone2 == 100.0 * 2 + 200.0 * 3


def test_add_base_products(product):
    assert product + product == 100.0


def test_add_different_classes(phone, grass):
    with pytest.raises(TypeError):
        phone + grass


def test_add_parent_and_child(phone, product):
    with pytest.raises(TypeError):
        phone + product


def test_category_add_product(phone, grass, product):
    category = Category("Тест", "Описание")
    category.add_product(phone)
    category.add_product(grass)
    category.add_product(product)
    assert "Samsung" in category.products
    assert str(category) == "Тест, количество продуктов: 17 шт."


def test_category_add_invalid(phone):
    category = Category("Тест", "Описание", [phone])
    for bad in ("строка", 123, None, {"name": "x"}):
        with pytest.raises(TypeError):
            category.add_product(bad)


def test_category_counters(phone):
    before_c, before_p = Category.category_count, Category.product_count
    Category("Новая", "Описание", [phone])
    assert Category.category_count == before_c + 1
    assert Category.product_count == before_p + 1
