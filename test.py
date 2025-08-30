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


def get_tree():
    def build_node(category_id):
        subcat = [cat for cat in categories if cat["parent_id"] == category_id]
        for cat in subcat:
            cat["children"] = build_node(cat["id"])
        return subcat

    return build_node(None)


print(get_tree())

tree = [
    {
        "id": 1,
        "name": "Электроника",
        "children": [
            {
                "id": 2,
                "name": "Компьютеры",
                "children": [
                    {"id": 3, "name": "Ноутбуки", "children": []},
                    {"id": 4, "name": "Настольные ПК", "children": []},
                ],
            },
            {"id": 5, "name": "Смартфоны", "children": []},
            {
                "id": 6,
                "name": "Аксессуары",
                "children": [
                    {"id": 7, "name": "Наушники", "children": []},
                    {"id": 8, "name": "Зарядные устройства", "children": []},
                ],
            },
        ],
    },
    {
        "id": 9,
        "name": "Одежда",
        "children": [
            {
                "id": 10,
                "name": "Мужская одежда",
                "children": [
                    {"id": 11, "name": "Футболки", "children": []},
                    {"id": 12, "name": "Куртки", "children": []},
                ],
            },
            {
                "id": 13,
                "name": "Женская одежда",
                "children": [
                    {"id": 14, "name": "Платья", "children": []},
                    {"id": 15, "name": "Юбки", "children": []},
                ],
            },
        ],
    },
    {
        "id": 16,
        "name": "Книги",
        "children": [
            {
                "id": 17,
                "name": "Художественная литература",
                "children": [
                    {"id": 18, "name": "Фантастика", "children": []},
                    {"id": 19, "name": "Детективы", "children": []},
                ],
            },
            {"id": 20, "name": "Учебники", "children": []},
        ],
    },
]

tree2 = [
    {
        "id": 1,
        "name": "Электроника",
        "parent_id": None,
        "childrem": [
            {
                "id": 2,
                "name": "Компьютеры",
                "parent_id": 1,
                "children": [
                    {"id": 3, "name": "Ноутбуки", "parent_id": 2, "children": []},
                    {"id": 4, "name": "Настольные ПК", "parent_id": 2, "children": []},
                ],
            },
            {"id": 5, "name": "Смартфоны", "parent_id": 1, "children": []},
            {
                "id": 6,
                "name": "Аксессуары",
                "parent_id": 1,
                "children": [
                    {"id": 7, "name": "Наушники", "parent_id": 6, "children": []},
                    {
                        "id": 8,
                        "name": "Зарядные устройства",
                        "parent_id": 6,
                        "children": [],
                    },
                ],
            },
        ],
    },
    {
        "id": 9,
        "name": "Одежда",
        "parent_id": None,
        "childrem": [
            {
                "id": 10,
                "name": "Мужская одежда",
                "parent_id": 9,
                "children": [
                    {"id": 11, "name": "Футболки", "parent_id": 10, "children": []},
                    {"id": 12, "name": "Куртки", "parent_id": 10, "children": []},
                ],
            },
            {
                "id": 13,
                "name": "Женская одежда",
                "parent_id": 9,
                "children": [
                    {"id": 14, "name": "Платья", "parent_id": 13, "children": []},
                    {"id": 15, "name": "Юбки", "parent_id": 13, "children": []},
                ],
            },
        ],
    },
    {
        "id": 16,
        "name": "Книги",
        "parent_id": None,
        "childrem": [
            {
                "id": 17,
                "name": "Художественная литература",
                "parent_id": 16,
                "children": [
                    {"id": 18, "name": "Фантастика", "parent_id": 17, "children": []},
                    {"id": 19, "name": "Детективы", "parent_id": 17, "children": []},
                ],
            },
            {"id": 20, "name": "Учебники", "parent_id": 16, "children": []},
        ],
    },
]
