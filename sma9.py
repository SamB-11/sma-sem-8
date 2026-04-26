"""https://www.kaggle.com/datasets/cagrickr/social-media-post-engagement-dataset"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\DELL\Downloads\social_media_engagement_dataset.csv")

avg = df.groupby("platform")[["likes","comments","shares"]].mean()

print(avg)

avg.plot(kind='bar')

plt.show()

"""pip install pandas matplotlib"""
