import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: Revenue vs Units Sold
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Units_Sold', y='Revenue', data=df,c='fuchsia')
plt.title('Revenue vs Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# Correlation
correlation = df['Units_Sold'].corr(df['Revenue'])
print("Correlation between Units Sold and Revenue:", round(correlation, 2))
