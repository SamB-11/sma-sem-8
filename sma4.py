""" https://www.kaggle.com/datasets/rakeshrau/social-network-ads?utm_source=chatgpt.com """
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Samiksha Bokade\Downloads\Social_Network_Ads.csv")

# ----- EDA -----
print("Mean Age:", df["Age"].mean())
print("Median Salary:", df["EstimatedSalary"].median())
print("Mode Gender:", df["Gender"].mode()[0])
print("Variance Salary:", df["EstimatedSalary"].var())
print("Std Dev Age:", df["Age"].std())
print("Min Age:", df["Age"].min())
print("Max Salary:", df["EstimatedSalary"].max())
print("Skewness Salary:", df["EstimatedSalary"].skew())
print("Missing Values:\n", df.isnull().sum())
print("Correlation:\n", df[['Age','EstimatedSalary','Purchased']].corr())

# ----- Visualizations -----

plt.hist(df['Age']); plt.title("Age Distribution"); plt.show()

plt.boxplot(df['EstimatedSalary']); plt.title("Salary Distribution"); plt.show()

df['Gender'].value_counts().plot(kind='bar'); plt.title("Gender Count"); plt.show()

plt.scatter(df['Age'], df['EstimatedSalary']); plt.title("Age vs Salary"); plt.show()

plt.plot(df['Age']); plt.title("Age Trend"); plt.show()

plt.imshow(df[['Age','EstimatedSalary','Purchased']].corr())
plt.title("Heatmap"); plt.colorbar(); plt.show()

df['Purchased'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Purchased %"); plt.show()

"""
pip install pandas
pip install matplotlib

👉 If pip doesn’t work:

pip3 install pandas matplotlib
"""
