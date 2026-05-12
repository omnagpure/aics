from itertools import combinations

# Sample transactions
data = [
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter']
]

min_support = 2
items = ['Milk', 'Bread', 'Butter']

# Apriori logic
for i in range(1, len(items)+1):
    print("\nItemsets of size", i)
    for combo in combinations(items, i):
        count = 0
        for transaction in data:
            if set(combo).issubset(set(transaction)):
                count += 1
        if count >= min_support:
            print(combo, "Support =", count)