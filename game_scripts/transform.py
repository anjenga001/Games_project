import json
import pandas as pd


with open('pc_games_last_year.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.json_normalize(data)

df = df.drop(columns=['screenshots', 'micro_trailer', 'gameplay', 'short_description', 'image', 'link'])

df['year'] = df['year'].astype(int)
df['rating.count'] = df['rating.count'].astype('Int64')
df['rating.mean'] = df['rating.mean'].round(2)

df.dropna()
print(df.head())
