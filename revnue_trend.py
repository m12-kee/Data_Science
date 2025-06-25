import matplotlib.pyplot as plt
import seaborn as sns

# Sorting by date
df_sorted = df.sort_values('Date')

# Line plot: Revenue trend over time
plt.figure(figsize=(8, 4))
plt.plot(df_sorted['Date'], df_sorted['Revenue'], marker='*')
plt.title('Revenue Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
