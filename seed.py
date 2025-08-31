from src.core.database import session_maker
from src.products.models import Category, Product
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


products = [
    {
        "id": 1,
        "name": "MacBook Pro 16",
        "description": "Мощный ноутбук для работы и учебы",
        "price": 2500.00,
        "image": "media/2905_car222.jpeg",
        "user_id": 1,
        "category_id": 3,  # Ноутбуки
    },
    {
        "id": 2,
        "name": "iPhone 14 Pro",
        "description": "Флагманский смартфон Apple",
        "price": 1200.00,
        "image": "media/2905_car222.jpeg",
        "user_id": 1,
        "category_id": 5,  # Смартфоны
    },
    {
        "id": 3,
        "name": "Sony WH-1000XM5",
        "description": "Беспроводные наушники с шумоподавлением",
        "price": 400.00,
        "image": "media/2905_car222.jpeg",
        "user_id": 1,
        "category_id": 7,  # Наушники
    },
    {
        "id": 4,
        "name": "Футболка Nike",
        "description": "Хлопковая футболка для повседневной носки",
        "price": 35.00,
        "image": "media/2905_car222.jpeg",
        "user_id": 1,
        "category_id": 11,  # Футболки
    },
    {
        "id": 5,
        "name": "Учебник по математике",
        "description": "Алгебра и геометрия для студентов",
        "price": 20.00,
        "image": "media/2905_car222.jpeg",
        "user_id": 1,
        "category_id": 20,  # Учебники
    },
    {
        "id": 6,
        "name": "Платье Zara",
        "description": "Летнее платье средней длины",
        "price": 80.00,
        "image": "media/2905_car222.jpeg",
        "user_id": 1,
        "category_id": 14,  # Платья
    },
]


def add_products():
    with session_maker() as session:
        for p in products:
            new_p = Product(**p)
            session.add(new_p)
        session.commit()


def add_categories():
    with session_maker() as session:
        for cat in categories:
            new_cat = Category(**cat)
            session.add(new_cat)
        session.commit()


add_products()
