import pandas as pd
import requests
import time
from sqlalchemy import create_engine, text
import datetime
import psycopg2

token = 'CCZGkNSEEFRZwDQzvUuXcrhBTUuBjyunaslOOvZY'
df = pd.read_xml("https://discogs-data-dumps.s3-us-west-2.amazonaws.com/data/2023/discogs_20231001_labels.xml.gz")

df = df.drop(columns=['images', 'urls', 'sublabels'])
df = df[df['data_quality'] == 'Complete and Correct']
df = df.dropna(subset=['contactinfo'])
df = df.reset_index()
df = df.drop(columns = 'index')

responses = []

for label_id in df['id']:
    time.sleep(2)
    url = f"https://api.discogs.com/labels/{label_id}/releases"
    headers = {'Authorization': f'Discogs token={token}', 'User-Agent': 'labels_etl/1.0'}
    attempt = 0
    response = requests.get(url)
    while attempt < 4:
        if response.status_code == 200:
            responses.append(response.json())
            print('success')
            break
        elif response.status_code == 429:
            print("Rate limited. Retrying in 10 seconds...")
            time.sleep(10)
        else:
            print(f"Error for label ID {label_id}: {response.status_code}")
            break

        attempt += 1

df2 = pd.DataFrame(columns=['num_of_releases', 'max_release_year', 'min_release_year'])

for response in responses:
    releases = response.get('releases', [])

    release_years = [release['year'] for release in releases if release['year'] > 0]

    num_releases = len(release_years) if release_years else 0
    max_year = max(release_years) if release_years else None
    min_year = min(release_years) if release_years else None

    temp_df = pd.DataFrame({'num_of_releases': [num_releases], 'max_release_year': [max_year], 'min_release_year': [min_year]})

    df2 = pd.concat([df2, temp_df], ignore_index=True)

completed_df = pd.concat([df, df2], axis=1)

completed_df = completed_df[completed_df['num_of_releases'] > 0]

completed_df['num_of_releases'] = completed_df['num_of_releases'].astype(int)
completed_df['max_release_year'] = completed_df['max_release_year'].astype(int)
completed_df['min_release_year'] = completed_df['min_release_year'].astype(int)

host = "localhost"
database = "labels"
user = "bonks"
password = "bonks"
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}')
completed_df.to_sql('labels', engine, if_exists='replace', index=False)