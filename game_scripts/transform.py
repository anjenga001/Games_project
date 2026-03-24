import json
import pandas as pd


with open('pc_games_last_year.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.json_normalize(data)

df = df.drop(columns=['screenshots', 'micro_trailer', 'gameplay', 'short_description', 'image', 'link'])

df = df[['id', 'name', 'year', 'rating.mean', 'rating.count']]

df['year'] = df['year'].astype(int)
df['rating.count'] = df['rating.count'].astype('Int64')
df['rating.mean'] = df['rating.mean'].round(2)

df = df.dropna()

df = df.drop_duplicates(subset='id', keep='first')


df.to_csv('games_last_year.csv', index=False)