import json
from pprint import pprint
import problem_b


def books_info(books, categories):
    # 여기에 코드를 작성합니다.
    books_info_list = []
    for book in books:
        books_info_list.append(problem_b.book_info(book, categories))
    return books_info_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open(
        current_dir / 'data' / 'categories.json', encoding='utf-8'
    )
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
