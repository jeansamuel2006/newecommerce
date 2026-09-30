import json
from pathlib import Path

from src.category import Category
from src.product import Product
from src.utils import load_data


def test_load_data(tmp_path: Path) -> None:
    data = [
        {
            "name": "Смартфоны",
            "description": "Категория",
            "products": [
                {
                    "name": "iPhone 15",
                    "description": "512GB",
                    "price": 210000.0,
                    "quantity": 8,
                }
            ],
        }
    ]
    file = tmp_path / "products.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    categories = load_data(str(file))

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "iPhone 15"
    assert categories[0].products[0].price == 210000.0
