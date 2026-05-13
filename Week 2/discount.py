purchase_amount = float(input("Enter purchase amount in €: "))

if purchase_amount >= 200:
    discount_percentage = 15
elif purchase_amount >= 100:
    discount_percentage = 10
elif purchase_amount >= 50:
    discount_percentage = 5
else:
    discount_percentage = 0

discount_amount = purchase_amount * (discount_percentage / 100)

new_purchase_amount = purchase_amount - discount_amount

print(f"Your discount: {discount_amount:.2f}")

if discount_percentage > 0:
    print(f"Discount ({discount_percentage}%): €{discount_amount:.2f}")
    print(f"Total to pay: €{new_purchase_amount:.2f}")
else:
    print("No discount applicable.")
    print(f"Total to pay: €{purchase_amount:.2f}")