"""
    팔로워가 5,000,000 이상, 10,000,000 미만인 아티스트의 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
from pathlib import Path

current_dir = Path(__file__).resolve().parent

artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
artists = json.load(artist_json)


def get_popular():
    # 여기에 코드를 작성합니다.
    global artists
    famous_artists = []
    for artist in artists:
        artist_id = artist['id']
        id_json = open(current_dir / 'data' / 'artists'/f"{artist_id}.json", encoding='utf-8')
        id = json.load(id_json)
        if id['followers']['total'] < 10000000 and id['followers']['total'] >= 5000000:
            famous_artists.append({'followers' : id['followers']['total'],'name':id['name']})
    return famous_artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_popular())
