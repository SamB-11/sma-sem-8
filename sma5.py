""" https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset?utm_source=chatgpt.com """
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\Samiksha Bokade\Downloads\Tweets.csv")[['text']].dropna()
print("Original:\n", df.head(2))

# Lowercase
df['text'] = df['text'].str.lower()
print("\nLowercase:\n", df.head(2))

# Sentiment polarity
df['polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
print("\nPolarity:\n", df[['text','polarity']].head(10))

# Label sentiment
df['sentiment'] = df['polarity'].apply(
    lambda x: "Positive" if x>0 else ("Negative" if x<0 else "Neutral"))
print("\nSentiment:\n", df[['text','sentiment']].head(10))

# Tweet length
df['length'] = df['text'].apply(lambda x: len(x.split()))
print("\nLength:\n", df[['text','length']].head(2))

# Summary
print("\nSentiment Count:\n", df['sentiment'].value_counts())

# Top words
words = ' '.join(df['text']).split()
from collections import Counter
print("\nTop Words:", Counter(words).most_common(10))

# Graph
df['sentiment'].value_counts().plot(kind='bar')
plt.title("Sentiment Analysis")
plt.show()

""" pip install pandas
pip install matplotlib
pip install textblob
Then (VERY IMPORTANT):
python -m textblob.download_corpora
"""
