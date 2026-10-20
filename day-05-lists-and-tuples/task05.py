products = ["T-Shirt", "Jeans", "Sneakers", "Watch", "Cap", "Jacket"]
prices = [799, 1499, 2999, 1999, 399, 3499]

# 1. Slicing
print("First 3:", products[0:3])
print("Last 2:", products[-2:])

# 2. Add new product
products.append("Sunglasses")
prices.append(1299)

# 3. Remove Cap from both lists
cap_index = products.index("Cap")
print("Index of Cap:", cap_index)
products.pop(cap_index)
prices.pop(cap_index)

# 4. Price summary
print("Cheapest:", min(prices))
print("Costliest:", max(prices))
print("Average:", sum(prices) / len(prices))

# 6. Sort low to high with prices
pairs = []
for i in range(len(products)):
    pairs.append([products[i], prices[i]])

pairs.sort(key=lambda pair: pair[1])

print("Sorted by price:")
for name, price in pairs:
    print(f"{name:12} Rs. {price}")

# 7. Shop location as a tuple
shop_location = (8.1833, 77.4119)
lat, lng = shop_location
print(f"Latitude {lat}, Longitude {lng}")

# Bonus: numbered catalog
print("----- Catalog -----")
for index, (name, price) in enumerate(zip(products, prices), start=1):
    print(f"{index}. {name:12} Rs. {price}")
