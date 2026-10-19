# Day 01:Variables and data types

# ---------- 1. Creating variables ----------
product_name="Nike Running shoes"     #str(text)
brand="nike"                          #str
price=3499                            #int(whole)
discount_percent=20.5                 #float(decimal)
rating=4.3                            #float
in_stock=True                         #bool(true/false)
coupon_code=None                      #None(no value yet)

# ---------- 2. Printing variables ----------
print("product:",product_name)
print("brand:",brand)
print("price",price)
print("discount",discount_percent)
print("rating",rating)
print("in stock",in_stock)
print("coupon",coupon_code)

# ---------- 3. Checking the type of a variable ----------
print("-------types------")
print(type(product_name))
print(type(price))
print(type(discount_percent))
print(type(in_stock))
print(type(coupon_code))

# ---------- 4. Doing maths with variables ----------
discount_amount=price*discount_percent/100
final_price=price-discount_amount
print("------------price calculations---------")
print("discount amount:",discount_amount)
print("final price",final_price)

# ---------- 5. Changing a variable ----------
price=3999
print("New price:",price)

# ---------- 6. Multiple assignment ----------
size,color="M","Black"
print("size:",size,"|color:",color)

# ---------- 7. Joining text ----------
full_title=brand+"-"+product_name
print(full_title)

# ---------- 8. f-strings (the best way to mix text and variables) ----------
print(f"{product_name} costs rs.{price} and is rated {rating} stars.")


# ---------- 9. Type conversion ----------
price_text="2999"
price_number=int(price_text)
print(price_number +1)
print(str(price)+"rupees")

# ---------- 10. Useful string methods ----------
name="    Stylekart   "
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(len(name.strip()))