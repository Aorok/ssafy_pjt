import json
from pprint import pprint

def artist_info(artist,genres_list):
    # 여기에 코드를 작성합니다.
    artist_info_dict = {}
    #변수 
    
    id = artist['id']
    
    name = artist['name']
    
    genres_ids = artist['genres_ids']

    images = artist['images']

    type = artist ['type']

    artist_genres_names = []
     
    # artist_info_dict에 key, value 전달
    for genres in genres_list[::-1]:
        if genres['id']in genres_ids: artist_genres_names.append(genres['name']) 
    artist_info_dict['name'] = name
    artist_info_dict['id'] = id
    artist_info_dict['images'] = images
    artist_info_dict['type'] = type

    artist_info_dict['genres_names'] = artist_genres_names
    
    return artist_info_dict



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
