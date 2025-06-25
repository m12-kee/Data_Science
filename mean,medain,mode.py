# Mean, Median, Mode for Profit
mean_profit = df['Profit'].mean()
median_profit = df['Profit'].median()
mode_profit = df['Profit'].mode()[0]

print("Mean Profit:", mean_profit)
print("Median Profit:", median_profit)
print("Mode Profit:", mode_profit)

# Group by Product and calculate std deviation of Revenue
revenue_std = df.groupby('Product')['Revenue'].std()

print("Standard Deviation of Revenue by Product:")
print(revenue_std)
