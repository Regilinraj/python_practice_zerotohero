#      Ask for: customer name, cart total (float), membership type (gold, silver, or none), and coupon code
#      Apply the member discount:
#      gold gets 15%
#      silver gets 10%
#      none gets 0%
#      If the coupon is EXTRA5, give an additional 5% off the already discounted amount
#      If the amount after discounts is 1000 or more, delivery is free. Otherwise add Rs. 79
#      Print the bill:
#      ------ CHECKOUT ------
#      Customer      : Regilin
#      Membership    : gold
#      Cart total    : Rs. 2000.00
       #Member discount: Rs. 300.00
#      Coupon discount: Rs. 85.00
#      Delivery      : Rs. 0.00
#      Amount to pay : Rs. 1615.00

customer_name=input("Enter customer name: ")
cart_total=float(input("Enter cart total: "))
membership=input("Enter membership(gold,silver,none): ").strip().lower()
coupon_code=input("Enter coupon code(press enter to skip): ").strip().upper()

if membership=="gold":
    discount_percent=15
elif membership=="silver":
    discount_percent=10
elif membership=="none":
    discount_percent=0
else:
    print("Invalid membership,treating as none")
    membership="none"
    discount_percent=0

member_discount=cart_total*discount_percent/100
after_member_discount=cart_total-member_discount

coupon_discount=0
if coupon_code=="EXTRA5":
    coupon_discount=after_member_discount*5/100
amount_after_discounts=after_member_discount-coupon_discount

if amount_after_discounts>=1000:
    delivery=0
else:
    delivery=79

amount_to_pay=amount_after_discounts+delivery

print("\n-----------CHECKOUT----------")
print(f"Customer              : {customer_name}")
print(f"Membership            : {membership}")
print(f"cart total            : Rs. {cart_total:.2f}")
print(f"Membership discount   : Rs. {member_discount:.2f}")
print(f"Coupon discount       : Rs. {coupon_discount:.2f}")
print(f"delivery              : Rs. {delivery:.2f}")
print(f"Amount to pay         : Rs. {amount_to_pay:.2f}")



