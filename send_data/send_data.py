import pandas as pd
import requests
import os

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(os.getcwd(), 'data', 'keyword_posts.csv'))

    for index, row in df.iterrows():

        requests.post("https://localhost:8000/api/v1/contents/", {
            "keyword": row['keyword'],
            "video_url": row['video_url'],
            'video_caption': row['video_caption'],
            'author_username': row['author_username'],
            'author_url': row['author_url'],
            'following_count': row['following_count'],
            'followers_count': row['followers_count'],
            'likes_count': row['likes_count']
        })