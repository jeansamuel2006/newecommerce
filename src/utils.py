import json
from typing import Any

from src.category import Category
from src.product import Product


def load_data(path: str) -> list[Category]:
    with open(path, encoding="utf-8") as f:
        data: list[dict[str, Any]] = json.load(f)
    categories = []
    for cat in data:
        products = [Product(**p) for p in cat["products"]]
        categories.append(Category(cat["name"], cat["description"], products))
    return categories
