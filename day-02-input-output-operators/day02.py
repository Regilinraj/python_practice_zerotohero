# Day 02: Input, Output and Operators

# ---------- 1. print() options ----------

print("Welcome to styleKart")
print("shirt","Jeans","Shoes")        #separated by space
print("shirt","Jeans","Shoes",sep="|")       #custom seperator
print("Loading",end=".....")               #no new line at the end
print("done")
print("Line1\nLine2")                      #\n-new line
print("Name:\tRegilin")                    #\t-tab space

# ---------- 2. input() always returns text ----------

customer_name=input("Enter your name: ")
print(f"Hello, {customer_name}!")

# ---------- 3. Converting input to numbers ----------

price=float(input("Enter product price: "))
quantity=int(input("Enter quantity: "))
print("price converted to float",price)
print("quantity converted to int",quantity)

# ---------- 4. Arithmetic operators ----------

subtotal=price*quantity
gst=subtotal*18/100
total=subtotal+gst

print("\n---------BILL----------")
print(f"Customer : {customer_name}")
print(f"Subtotal : Rs.{subtotal}")
print(f"GST(18%) : Rs.{gst}")
print(f"Total : Rs.{total}")

# ---------- 5. Formatting decimals ----------

print(f"Total (2 decimals): Rs.{total:.2f}")

# ---------- 6. Floor division and remainder ----------

items=17
box_size=5
full_boxes=items//box_size
leftover=items%box_size
print(f"{items} items={full_boxes} full boxes + {leftover} leftover")

# ---------- 7. Power ----------

print("2 to the power 5=",2**5)

# ---------- 8. Comparison operators ----------

print("------comparison-----")
print(total>1000)
print(quantity==1)
print(price!=0)

# ---------- 9. Logical operators ----------

free_delivery=total>999 and quantity>=1
print("free delivery:",free_delivery)

is_member=False
gets_discount=total>5000 or is_member
print("gets discount:",gets_discount)
print("not a member:",not is_member)

# ---------- 10. Assignment operators ----------

wallet=1000
wallet-=250    #wallet=wallet-250
print("after purchase:",wallet)
wallet+=100     #wallet=wallet+100
print("after refund:",wallet)
wallet*=2        #wallet=wallet*2
print("Doubled:",wallet)

