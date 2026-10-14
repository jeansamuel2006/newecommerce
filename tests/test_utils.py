import json
from pathlib import Path

from src.category import Category
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
    assert "iPhone 15" in categories[0].products
    assert "210000.0" in categories[0].products
