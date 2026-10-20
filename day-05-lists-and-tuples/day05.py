# Day 05: Lists and Tuples

# ---------- 1. Creating lists ----------
sizes=["S","M","L","XL","XXL"]
prices=[234,678,900,600,600]
mixed=["t-shirt",45,5.6,True]    #list can hold different types
empty_cart=[]

print(sizes)
print(len(sizes))                 #number of items

# ---------- 2. Indexing ----------
print(sizes[0])      #first item
print(sizes[2])      #third item
print(sizes[-1])     #last item
print(sizes[-2])     #second last

# ---------- 3. Slicing: [start:stop:step] ----------
numbers=[10,20,30,40,50,60]
print(numbers[1:4])           # [20, 30, 40]  (stop is excluded)
print(numbers[:3])            # first 3 items
print(numbers[3:])            # from index 3 to the end
print(numbers[::2])           # every second item
print(numbers[::-1])          # reversed copy

# ---------- 4. Changing items ----------
sizes[0]="XS"
print(sizes)

# ---------- 5. Adding items ----------
cart=[]
cart.append("T-shirt")
cart.append("Jeans")
cart.insert(1,"cap")          #insert at position 1
print(cart)

more_item=["watch","belt"]
cart.extend(more_item)
print(cart)

# ---------- 6. Removing items ----------
cart.remove("cap")         #remove by value
print(cart)

last_item=cart.pop()        #remove and get the last item
print("Removed:",last_item)

first_item=cart.pop(0)       #remove item at index 0
print("Removed:",first_item)
print("Cart Now: ",cart)

del cart[0]                   #delete by index
print("after del: ",cart)

# ---------- 7. Checking items ----------
products = ["T-Shirt", "Jeans", "Sneakers", "Jeans"]
print("Jeans" in products)
print(products.count("Jeans"))
print(products.index("Sneakers"))

# ---------- 8. Sorting ----------
prices = [799, 1499, 2999, 599]
prices.sort()
print("Low to high: ",prices)

prices.sort(reverse=True)
print("High to Low: ",prices)

original=[30,10,20]
sorted_copy=sorted(original)
print(original,sorted_copy)

# ---------- 9. Useful built-in functions ----------

prices = [799, 1499, 2999, 599]
print("Total:", sum(prices))
print("Cheapest:", min(prices))
print("Costliest:", max(prices))
print("Average:", sum(prices) / len(prices))

# ---------- 10. Looping with lists ----------
for index,price in enumerate(prices):
    print(f"Item {index}: Rs. {price}")

# ---------- 11. Joining and splitting text ----------
tags = ["cotton", "slim-fit", "casual"]
print(", ".join(tags))

text="red,green,blue"
print(text.split(","))

# ---------- 13. Copying lists (important!) ----------
a=[1,2,3]
b=a                   # NOT a copy, both names point to ONE list
b.append(4)
print(a,b)            # [1, 2, 3, 4]  a changed too!

c=a.copy()            # a real copy
c.append(5)
print(c,a)            # a is unchanged

# ---------- 14. Nested lists (a list inside a list) ----------

catalog=[
    ["T-shirt",799],
    ["jeans",1499],
    ["sneakers",2999]
    ]
print(catalog[1])
print(catalog[1][1])
print(catalog[1][0])

for name,price in catalog:
    print(f"{name} costs Rs. {price}")


# ---------- 15. Tuples (cannot be changed) ----------

location = (8.1833, 77.4119)
print(location[0])
print(len(location))

lat,lng=location                            #unpacking
print(f"latitude {lat} longitude {lng}")

single=(5,)                           #a one item tuple needs comma
not_tuple=(5)
print(type(single))                    #tuple
print(type(not_tuple))                 #int

# location[0] = 10                    # ERROR: tuples cannot be changed


# ---------- 16. Unpacking lists too ----------
first,second,*rest=[10,20,30,40,50,60]
print(first,second,rest)

*start,last=[10,20,30,40]
print(start,last)

start,*middle,last=[10,20,30,40,50]
print(start,middle,last)

# ---------- 17. Swapping values ----------

x,y=10,20
y,x=x,y
print(x,y)