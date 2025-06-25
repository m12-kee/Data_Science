from scipy.stats import chi2_contingency

# Cross-tab between Sales Rep and Product (simulated demographic vs preference)
contingency_table = pd.crosstab(df['Sales_Rep'], df['Product'])
contingency_table
# Chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("Chi-squared value:", round(chi2, 2))
print("P-value:", round(p, 4))
if p < 0.05:
    print("There is a significant relationship between Sales Rep and Product preference.")
else:
    print("No significant relationship found.")
