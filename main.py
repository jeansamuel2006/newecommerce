from src.utils import load_data

categories = load_data("data/products.json")
for c in categories:
    print(c.name, len(c.products))