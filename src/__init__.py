# category_id, title,        parent_id

# 1,          Транспорт,     null
# 2,          Продажа Авто,  1
# 3,          Ремонт Авто,   1
# 4,          Honda,         2


"""
def tree(categories):
    subcategories = category....
    if subcategories > 0:
        for i in subcategories:
            categories.append(tree(categories))


{
    "id":1,
    "title":"...",
    parent_id:null
    childs:{
        "id":2,
        "title":"...",
        parent_id:1
        childs:{
            "id":3,
            "title":"...",
            parent_id:2
            childs:{
                ""
            }
        }
    }

}

cache(categories)
12 часов


"""
