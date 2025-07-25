"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint
from pathlib import Path

current_dir = Path(__file__).resolve().parent
artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
artists = json.load(artist_json)

genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
genres_list = json.load(genres_json)

def acoustic_artists():

    global artists
    acoustic_artists_list = []
    for artist in artists:
        # 339는 acoustic id number이다.
        if 339 in artist['genres_ids']:  
            acoustic_artists_list.append(artist['name'])
    return acoustic_artists_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(acoustic_artists())
