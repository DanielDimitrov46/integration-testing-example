import pytest
from order_module import calculate_total_price
from discount_module import apply_discount


# Mock функция за get_product
def mock_get_product(product_id):
    products = {
        1: {"price": 300},
        2: {"price": 600},
        3: {"price": 1200}
    }
    return products.get(product_id, None)


def test_apply_discount():
    assert apply_discount(1500) == 1350  # 10% отстъпка
    assert apply_discount(1000) == 950  # 5% отстъпка
    assert apply_discount(750) == 712.5  # 5% отстъпка
    assert apply_discount(500) == 500  # Без отстъпка
    assert apply_discount(300) == 300  # Без отстъпка


# Тест за calculate_total_price с mock на get_product
def test_calculate_total_price(monkeypatch):
    monkeypatch.setattr("order_module.get_product", mock_get_product)

    assert calculate_total_price([(1, 1)]) == 300  # Без отстъпка
    assert calculate_total_price([(1, 2)]) == 570  # 5% отстъпка
    assert calculate_total_price([(2, 1)]) == 570  # 5% отстъпка
    assert calculate_total_price([(3, 1)]) == 1080  # 10% отстъпка