from src.utils import load_data

categories = load_data("data/products.json")
for category in categories:
    print(category.name)
    print(category.products)
