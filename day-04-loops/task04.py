#   Start with this data:
#   python

#   products = ["T-Shirt", "Jeans", "Sneakers", "Watch", "Cap"]
#   prices = [799, 1499, 2999, 1999, 399]
#   quantities = [2, 1, 1, 1, 3]
#   Your program must:

#   Use a for loop with zip to print each line as: T-Shirt x 2 = Rs. 1598
#   Calculate and print the grand total
#   Find and print the most expensive item (without using max, use a loop)
#   Use continue to print only items whose line total is above 1000
#   Use a while loop to ask the user for a coupon code until they enter STYLE20 or type skip
#   Bonus: print a numbered bill using enumerate, and a star pattern of this shape:

#   *
#   **
#   ***
#   **
#   *


products = ["T-Shirt", "Jeans", "Sneakers", "Watch", "Cap"]
prices = [799, 1499, 2999, 1999, 399]
quantities = [2, 1, 1, 1, 3]
for product,quantity,price in zip(products,quantities,prices):
    print(f"{product} * {quantity} = Rs.{price*quantity}")

total = 0
for price, quantity in zip(prices, quantities):
    total += price * quantity
print("Grand total: Rs.", total)

most_expensive_name=products[0]
most_expensive_price=prices[0]
for name,price in zip(products,prices):
    if price>most_expensive_price:
        most_expensive_price=price
        most_expensive_name=name
print(f"\nMost expensive item: {most_expensive_name} (Rs. {most_expensive_price})")

for name,price,qty in zip(products,prices,quantities):
    line_total=price*qty
    if line_total<=1000:
        continue
    print(f"{name}: Rs. {line_total}")

coupon=""
while coupon!="style20" and coupon!="skip":
    coupon=input("enter coupon code or skip: ").strip().lower()

if coupon=="style20":
    final_amount=total*0.80
    print(f"STYLE20 applied. Amount to pay: Rs. {final_amount:.2f}")
else:
    print(f"No coupon. Amount to pay: Rs. {total:.2f}")

print("\n------ NUMBERED BILL ------")
for number, (name, price, qty) in enumerate(zip(products, prices, quantities), start=1):
    print(f"{number}. {name:10} x {qty} = Rs. {price * qty}")

print("\n------ PATTERN ------")
for row in range(1, 4):
    print("*" * row)
for row in range(2, 0, -1):
    print("*" * row)

