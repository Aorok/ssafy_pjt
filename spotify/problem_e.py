import json
from pprint import pprint


def dec_artists(artists):
    # 여기에 코드를 작성합니다.

    famous_artists = []
    for artist in artists:
        artist_id = artist['id']
        id_json = open(current_dir / 'data' / 'artists'/f"{artist_id}.json", encoding='utf-8')
        id = json.load(id_json)
        if id['followers']['total'] >= 10000000:
            famous_artists.append({'name':id['name'],'uri-id':id['uri'].split(':')[2]})
    return famous_artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    pprint(dec_artists(artists_list))
