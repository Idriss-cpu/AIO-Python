# Controlling the Actions.
sun = "down"
if sun == "down":
    print("Good night")
print("I am here" + "\n")
total = 100
sales_tax_rate = 0.065
taxable = False
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sal_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sal_tax:.2f}")
    total = total + sal_tax
print(f"Total    : ${total:.2f}")

