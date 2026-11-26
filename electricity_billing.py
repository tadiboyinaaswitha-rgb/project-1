n = int(input("Enter number of months: "))
units_list = []
bills_list = []

for i in range(n):
    units = float(input(f"Enter units consumed in Month {i + 1}: "))
    if units < 0:
        print("Invalid units entered. Skipping month.")
        continue
    if units <= 100:
        cost = units * 3.0
    elif units <= 200:
        cost = (100 * 3.0) + (units - 100) * 5.0
    else:
        cost = (100 * 3.0) + (100 * 5.0) + (units - 200) * 8.0

    bill = cost + 50.0
    if units <= 80:
        bill = bill * 0.90
    elif units > 300:
        bill = bill * 1.15

    units_list.append(units)
    bills_list.append(round(bill, 2))

print("\n----- ELECTRICITY BILL SUMMARY -----")
for i in range(len(bills_list)):
    print(f"Month {i + 1}: Units = {units_list[i]} | Bill = Rs. {bills_list[i]}")
    if i > 0 and bills_list[i] > bills_list[i - 1] * 1.30:
        print(f"  -> ALERT: Unusual spike compared to Month {i}!")
print("Total Amount Payable: Rs.", round(sum(bills_list), 2))
