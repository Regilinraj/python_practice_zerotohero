#Ask the user for: customer name, product name, price (float), quantity (int)
#Calculate: subtotal, 10% discount, GST of 18% on the discounted amount, final total
#If the final total is above 1000, set free_delivery to True, otherwise False



customer_name=input("Enter your name: ")
product_name=input("Enter product name: ")
price=float(input("Enter the price: "))
quantity=int(input("Enter the quantity: "))

subtotal=price*quantity
discount_amount=subtotal*10/100
total_after_discount=subtotal-discount_amount
gst=total_after_discount*18/100
final_total=total_after_discount+gst

print("--------STYLEKART BILL--------")
print("customer:",customer_name)
print("product:",product_name)
print("Quantity:",quantity)
print("Subtotal:",subtotal)
print("Discount:",discount_amount)
print("GST:",gst)
print("Total:",final_total)
delivery=final_total>1000
print("Free delivery",delivery)
