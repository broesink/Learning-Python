price = float(input("Enter a price in €: "))

usd_rate = 1.08
gbp_rate = 0.86

print(f"Your amount converted in American dollars: ${price * usd_rate:.2f}")

print(f"Your amount converted in British pounds: £{price * gbp_rate:.2f}")