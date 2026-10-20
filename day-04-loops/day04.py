# Day 04: Loops

# ---------- 1. for loop over a list ----------
products=["jeans","T-shirt","sneakers","watch"]
for product in products:
    print("product:",product)

# ---------- 2. for loop with range ----------
print("------counting-------")
for i in range(5):
    print(i)

for i in range(1,5):
    print("Number: ",i)

for i in range(0,11,2):
    print("even:",i)

# ---------- 3. Looping over text ----------
for letter in "STYLE":
    print(letter)

# ---------- 4. Adding up values (running total) ----------
prices=[300,566,789,900,1000]
total=0
for price in prices:
    total+=price
print("Cart Total:",total)

# ---------- 5. enumerate: index plus item ----------
for index,product in enumerate(products,start=1):
    print(f"{index}.{product}")

# ---------- 6. Two lists together with zip ----------
for name,price in zip(products,prices):
    print(f"{name:10} Rs. {price}")

# ---------- 7. while loop ----------
print("-------countdown-----")
count=5
while count>0:
    print(count)
    count-=1
print("sales started")

# ---------- 8. while with user input ----------
password=""
while password!="style10":
    password=input("Enter password: ")
print("Login successfull!")

# ---------- 9. break: stop early ----------
print("--------search-------")
for product in products:
    if product=="jeans":
        print("Found jeans!")
        break
    print("checking,",product)

# ---------- 10. continue: skip one round ----------
print("----- Skip expensive items -----")
for price in prices:
    if price>500:
        continue
    print("affordable",price)

# ---------- 11. for...else ----------
search="jacket"
for product in products:
    if product==search:
        print("Found",search)
        break
else:
    print(search,"not in catalogue")

# ---------- 12. Nested loops ----------
print("----- Size and color combinations -----")
sizes=["S","M","L"]
colors=["black","white"]

for size in sizes:
    for color in colors:
        print(f"T-shirt-{size}-{color}")

# ---------- 13. Pattern printing ----------
print("----- Pattern -----")
for row in range(1,6):
    print("*"*row)

# ---------- 14. Multiplication table ----------
number=int(input("Enter a number for its table: "))
for i in range(1,11):
    print(f"{number}x{i}={number*i}")