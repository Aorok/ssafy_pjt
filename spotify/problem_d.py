import json


def max_popularity(artists):
  
    max_popularity_list =[]
    for artist in artists:
        artist_id = artist['id']
        id_json = open(current_dir / 'data' / 'artists'/f"{artist_id}.json", encoding='utf-8')
        id = json.load(id_json)
        max_popularity_list.append((id['name'],id['popularity']))
    
    best_artist =sorted(max_popularity_list,key=lambda x:x[1],reverse=True)[0][0]
    return best_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))
