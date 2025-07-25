import json


def sorted_cs_books_by_price(books, categories):
    # 여기에 코드를 작성합니다.
    #2721은 컴퓨터 공학 id  number이다.
    sorted_cs_books_by_price = []
    for book in books:
        if 2721 in book['categoryId']:
            sorted_cs_books_by_price.append((book['title'],book['priceSales']))
    sorted_cs_books_by_price = sorted(sorted_cs_books_by_price,key=lambda x:x[1],reverse=True)
    return [s[0] for s in sorted_cs_books_by_price]
                        

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

    print(sorted_cs_books_by_price(books, categories_list))
