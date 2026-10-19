#Stores these 7 variables for a T-shirt: name, brand, price (799), discount percent (10), size, rating, in-stock status
#Calculates the final price after discount
#Prints one clean line using an f-string, like:
#Roadster Cotton T-Shirt (Size M) - Rs. 719.1 - Rating: 4.1
#Prints the type of every variable




name="roadster cotton t-shirt"
brand="roadster"
price=799
discount_percent=10
size="M"
rating=4.1
inStockStatus=True
discount_amount=price*discount_percent/100
final_price=price-discount_amount
print(f"{name} (size {size}) - Rs.{final_price} - Rating {rating}")

print(type(name))
print(type(brand))
print(type(price))
print(type(discount_percent))
print(type(rating))
print(type(size))
print(type(inStockStatus))