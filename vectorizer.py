from sentence_transformers import SentenceTransformer
import numpy as np
import json
import pandas as pd
from tqdm.notebook import tqdm

model = SentenceTransformer('T-Systems-onsite/german-roberta-sentence-transformer-v2')

df = pd.read_json('data/lyrics.json')

print(df.head())

vectors = []
batch_size = 64
batch = []
# print(df.to_string())
# print(df)

for index, row in df.iterrows():

    print(row.artist)
    print('----------------------')
#     print(row.items())
    description = row.lyrics
    batch.append(description)
    if len(batch) >= batch_size:
        vectors.append(model.encode(batch))  # Text -> vector encoding happens here
        batch = []

if len(batch) > 0:
    vectors.append(model.encode(batch))
    batch = []

vectors = np.concatenate(vectors)
print(vectors)

np.save('data/vectors.npy', vectors, allow_pickle=False)