# Marginal probability: P(Product = Laptop)
prob_laptop = (df['Product'] == 'Laptop').mean()

# Joint probability: P(Product = Laptop and Region = North)
prob_joint = ((df['Product'] == 'Laptop') & (df['Region'] == 'North')).mean()

# Marginal for Region = North
prob_north = (df['Region'] == 'North').mean()

# Conditional probability: P(Region = North | Product = Laptop)
prob_cond = prob_joint / prob_laptop

# Union probability: P(Laptop or North) = P(A) + P(B) - P(A and B)
prob_union = prob_laptop + prob_north - prob_joint

print("P(Laptop):", round(prob_laptop, 2))
print("P(North):", round(prob_north, 2))
print("P(Laptop ∩ North):", round(prob_joint, 2))
print("P(North | Laptop):", round(prob_cond, 2))
print("P(Laptop ∪ North):", round(prob_union, 2))
