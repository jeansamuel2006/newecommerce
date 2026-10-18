import pytest

from src.product import BaseProduct, Product


def test_base_product_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseProduct()  # type: ignore[abstract]


def test_repr_format() -> None:
    product = Product("A", "B", 5.0, 3)
    assert repr(product) == "Product('A', 'B', 5.0, 3)"


def test_creation_logs_repr(capsys: pytest.CaptureFixture[str]) -> None:
    Product("Продукт1", "Описание", 1200, 10)
    out = capsys.readouterr().out
    assert "Product('Продукт1', 'Описание', 1200, 10)" in out
