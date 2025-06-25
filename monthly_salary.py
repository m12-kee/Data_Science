# Convert to monthly sales totals
monthly_sales = df.resample('M', on='Date')['Revenue'].sum()

# Plotting the trend
import matplotlib.pyplot as plt

plt.figure(figsize=(7, 4))
monthly_sales.plot(marker='*',color='orange')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()
