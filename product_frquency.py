import matplotlib.pyplot as plt
import seaborn as sns

# Frequency distribution of products sold
product_counts = df['Product'].value_counts()
print("Product Frequency:\n", product_counts)

# Plotting: Units Sold distribution
plt.figure(figsize=(6, 4))
sns.histplot(df['Units_Sold'], bins=5, kde=True,color='red')
plt.title('Units Sold Distribution')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.show()
