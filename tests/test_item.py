"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def item_instance():
    return Item("Смартфон", 10000, 20)

def test_item_creation(item_instance):
    assert item_instance.name == "Смартфон"
    assert item_instance.price == 10000
    assert item_instance.quantity == 20

def test_calculate_total_price(item_instance):
    assert item_instance.calculate_total_price() == 200000

def test_apply_discount(item_instance):
    item_instance.apply_discount()
    assert item_instance.price == 8000.0

def test_all_items_list(item_instance):
    assert item_instance in Item.all
