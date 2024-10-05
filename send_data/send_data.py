import pandas as pd
# import requests
import os

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(os.getcwd(), 'data', 'keyword_posts.csv'))

    df = df[:5]

    for index, row in df.iterrows():

        print(
            row['keyword'],
        row['video_url'],
        row['video_caption'],
        row['author_username'],
        row['author_url'],
        row['following_count'],
        row['followers_count'],
        row['likes_count']
        )