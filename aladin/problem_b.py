import json
from pprint import pprint


def book_info(book, categories):
    pass

    book_info_dict = {}
    
    author = book['author']
    
    id = book['id']
    
    title = book['title']
    
    categoryId = book['categoryId']

    description = book['description']

    cover = book ['cover']
    
    priceSales = book['priceSales'] 

    categoryName = []

    for category in categories:
        if category['id']in categoryId: categoryName.append(category['name']) 

    book_info_dict['author'] = author
    book_info_dict['id'] = id
    book_info_dict['title'] = title
    book_info_dict['categoryName'] = categoryName
    book_info_dict['description'] = description
    book_info_dict['cover'] = cover
    book_info_dict['priceSales'] = priceSales

    
    return book_info_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    book_json = open(current_dir / 'data' / 'book.json', encoding="utf-8")
    book = json.load(book_json)

    categories_json = open(
        current_dir / 'data' / 'categories.json', encoding="utf-8"
    )
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
