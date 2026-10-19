# Day 03: Conditions

# ---------- 1. Simple if ----------

cart_total=1200
if cart_total>999:
    print("You get free delivery!")

# ---------- 2. if / else ----------

if cart_total>999:
    delivery_charge=0
else:
    delivery_charge=99
print("Delivery Charge: " ,delivery_charge)

# ---------- 3. if / elif / else ----------

rating=4.3

if rating>=4.5:
    label="excellent"
elif rating>=4.0:
    label="very good"
elif rating>=3.0:
    label="good"
else:
    label="bad"
print(f"rating {rating} is {label}")

# ---------- 4. Combining conditions ----------

age=25
is_member=True

if age>=18 and is_member:
    print("Member offer unlocked")

if age<18 or age>60:
    print("special age discount")
else:
    print("no age discount")

# ---------- 5. Nested if ----------

is_logged_in=True
has_address=False

if is_logged_in:
    if has_address:
        print("Proceed to payment")
    else:
        print("please add a delivery address")
else:
    print("please login first")

# ---------- 6. The 'in' operator ----------

available_sizes=["S","M","L","XL"]
chosen_size="M"

if chosen_size in available_sizes:
    print(f"size {chosen_size} is available")
else:
    print(f"size {chosen_size} is out of stock")

if "XXL" not in available_sizes:
    print("XXL is not available")

# ---------- 7. Comparing text ----------

coupon=input("Enter Coupon Code: ").strip().upper()

if coupon=="STYLE20":
    print("20% discount applied")
elif coupon=="FIRST10":
    print("10% discount applied")
elif coupon=="":
    print("no coupon entered")
else:
    print("invalid coupon")

# ---------- 8. Truthiness ----------

user_name=""
if user_name:
    print("Hello,",user_name)
else:
    print("hello,Guest")

# ---------- 9. Ternary (one-line if/else) ----------

stock=0
status="In stock" if stock>0 else "out of stock"
print(status)

# ---------- 10. Chained comparison ----------

discount = 15
if 10 <= discount <= 20:
    print("Discount is in the 10 to 20 range")

# ---------- 11. Even or odd (using %) ----------

number=int(input("Enter a number: "))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")