# Categorize ratings for simplicity
df['Rating_Category'] = pd.cut(df['Customer_Rating'], bins=[4.0, 4.3, 4.6, 4.9], 
                               labels=['Low', 'Medium', 'High'])

# Frequency of rating categories
rating_freq = df['Rating_Category'].value_counts()
print("Rating Categories:\n", rating_freq)

# Bar graph of rating categories
plt.figure(figsize=(6, 4))
rating_freq.plot(kind='bar', color='blue')
plt.title('Customer Rating Categories')
plt.xlabel('Rating Level')
plt.ylabel('Number of Customers')
plt.show()
