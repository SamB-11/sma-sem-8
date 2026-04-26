"""https://www.kaggle.com/datasets/viditsanghvi/amazon-alexa-reviews-csv-file"""
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Samiksha Bokade\Downloads\amazon_alexa.csv")

# Remove null values
df = df.dropna()

# Preprocessing
df['review'] = df['verified_reviews'].str.lower()
df['review_length'] = df['verified_reviews'].str.len()

# Sentiment classification (keyword-based)
positive = df[df['review'].str.contains("good|great|happy|amazing|excellent", na=False)]
negative = df[df['review'].str.contains("bad|worst|sad|poor|terrible", na=False)]
neutral = df[~df.index.isin(positive.index) & ~df.index.isin(negative.index)]

df['sentiment'] = "Neutral"
df.loc[positive.index, "sentiment"] = "Positive"
df.loc[negative.index, "sentiment"] = "Negative"

# Plot sentiment
counts = [len(positive), len(neutral), len(negative)]
labels = ["Positive", "Neutral", "Negative"]

plt.bar(labels, counts)
plt.xlabel("Sentiment")
plt.ylabel("No of Reviews")
plt.title("Sentiment Analysis of Reviews")
plt.show()

# Ratings (if available)
if "rating" in df.columns:
    df['rating'].value_counts().plot(kind='bar')
    plt.title("Ratings")
    plt.show()

# Analysis
print(df.groupby("review_length").size().head())
print(df.groupby("sentiment")["review_length"].mean())

"""pip install pandas"""

pip install matplotlib

