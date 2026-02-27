''' Q20 : A distributor supplies mobile phones based on stock availability and payment status. Write
a program to implement the given policy and print appropriate messages. '''
stock_available = int(input("Enter the number of mobile phones in stock: "))
payment_status = input("Enter the payment status (paid/unpaid): ").strip().lower() 
if stock_available > 0:
    if payment_status == "paid":
        print("Mobile phone will be delivered.")
    elif payment_status == "unpaid":
        print("Payment pending. Mobile phone will be delivered once payment is received.")
    else:
        print("Invalid payment status. Please enter 'paid' or 'unpaid'.")
else:
    print("Mobile phone is out of stock. Please check back later.")


''' process - 2 '''
def delivery_status(stock_available, payment_status):
    payment_status = payment_status.strip().lower()
    if stock_available > 0:
        if payment_status == "paid":
            return "Mobile phone will be delivered."
        elif payment_status == "unpaid":
            return "Payment pending. Mobile phone will be delivered once payment is received."
        else:
            return "Invalid payment status. Please enter 'paid' or 'unpaid'."
    else:
        return "Mobile phone is out of stock. Please check back later."
stock_available = int(input("Enter the number of mobile phones in stock: "))
payment_status = input("Enter the payment status (paid/unpaid): ")
print(delivery_status(stock_available, payment_status))