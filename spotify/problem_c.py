import json
from pprint import pprint
import problem_b 

def artist_info(artists,genres_list):
    
    

    artist_info_list = []

    for artist in artists:
        artist_info_list.append(problem_b.artist_info(artist,genres_list))
    
    # 여기에 코드를 작성합니다.
   
   
    return artist_info_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
