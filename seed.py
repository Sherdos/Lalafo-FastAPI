from src.core.database import session_maker
from src.products.models import Category
import asyncio

categories = [
    {"id": 1, "name": "Электроника", "parent_id": None},
    {"id": 2, "name": "Компьютеры", "parent_id": 1},
    {"id": 3, "name": "Ноутбуки", "parent_id": 2},
    {"id": 4, "name": "Настольные ПК", "parent_id": 2},
    {"id": 5, "name": "Смартфоны", "parent_id": 1},
    {"id": 6, "name": "Аксессуары", "parent_id": 1},
    {"id": 7, "name": "Наушники", "parent_id": 6},
    {"id": 8, "name": "Зарядные устройства", "parent_id": 6},
    {"id": 9, "name": "Одежда", "parent_id": None},
    {"id": 10, "name": "Мужская одежда", "parent_id": 9},
    {"id": 11, "name": "Футболки", "parent_id": 10},
    {"id": 12, "name": "Куртки", "parent_id": 10},
    {"id": 13, "name": "Женская одежда", "parent_id": 9},
    {"id": 14, "name": "Платья", "parent_id": 13},
    {"id": 15, "name": "Юбки", "parent_id": 13},
    {"id": 16, "name": "Книги", "parent_id": None},
    {"id": 17, "name": "Художественная литература", "parent_id": 16},
    {"id": 18, "name": "Фантастика", "parent_id": 17},
    {"id": 19, "name": "Детективы", "parent_id": 17},
    {"id": 20, "name": "Учебники", "parent_id": 16},
]


def add_categories():
    with session_maker() as session:
        for cat in categories:
            new_cat = Category(**cat)
            session.add(new_cat)
        session.commit()


add_categories()
