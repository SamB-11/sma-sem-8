""" https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment """
import pandas as pd, re
from nltk.corpus import stopwords
import nltk; nltk.download('stopwords')

df = pd.read_csv(r"C:\Users\Samiksha Bokade\Downloads\Tweets.csv")
df = df[['text']].dropna().drop_duplicates()
print("Step 1: Loaded Data\n", df.head(3))

df['text'] = df['text'].str.lower()
print("\nStep 2: Lowercase\n", df.head(3))

df['text'] = df['text'].str.replace(r'@\w+|#', '', regex=True)
print("\nStep 3: Removed @ and #\n", df.head(3))

df['text'] = df['text'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
print("\nStep 4: Removed special characters\n", df.head(3))

df['tokens'] = df['text'].apply(lambda x: x.split())
print("\nStep 5: Tokenization\n", df[['tokens']].head(3))

stop_words = set(stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda x: [w for w in x if w not in stop_words])
print("\nStep 6: Stopwords removed\n", df[['tokens']].head(3))

df.drop_duplicates(subset='text', inplace=True)
print("\nStep 7: Duplicates removed\n", df.head(3))

df['text'] = df['text'].apply(lambda x: re.sub(r'(.)\1{2,}', r'\1', x))
print("\nStep 8: Normalized text\n", df.head(3))

df['word_count'] = df['text'].apply(lambda x: len(x.split()))
df = df[df['word_count'] > 3]
print("\nStep 9: Filtered short tweets\n", df[['text','word_count']].head(3))

print("\nFinal Cleaned Data:\n", df.head(5))

"""
pip install pandas
pip install nltk
"""
