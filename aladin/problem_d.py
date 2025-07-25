import json


def best_book(books):
    # 여기에 코드를 작성합니다.
    customer_Review_Rank_list =[]
    for book in books:
        book_id = book['id']
        id_json = open(current_dir / 'data' / 'books'/f"{book_id}.json", encoding='utf-8')
        id = json.load(id_json)
        customer_Review_Rank_list.append((id['title'],id['customerReviewRank']))
    
    best_book =sorted(customer_Review_Rank_list,key=lambda x:x[1],reverse=True)[0][0]
    return best_book

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    print(best_book(books))
