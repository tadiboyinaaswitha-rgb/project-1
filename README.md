# PROJECT 1 – PROGRESSIVE ELECTRICITY BILLING

## About the Project
The Progressive Electricity Billing project is designed to calculate monthly household electricity bills using slab-based tariff rates, fixed meter charges, low-usage rebates, and high-usage surcharges. It stores monthly consumption and bill amounts to compare spending across months and alert users whenever an unusual spike occurs compared to the previous month.

## Technologies Used
- **Python** – Used to develop the billing and spike-detection program.
- **Lists** – Used to store monthly consumed units and calculated bill amounts.
- **Loops** – Used to collect multi-month data and evaluate consecutive monthly bills.
- **Conditional Statements** – Used to apply slab rates, rebates, surcharges, and spike alerts.
- **Arithmetic Operators** – Used to compute slab charges, percentages, and totals.

## Main Features
- Accepts the number of months and units consumed for each month.
- Validates unit inputs to skip invalid negative readings.
- Calculates slab charges (`0–100` @ Rs. 3/unit, `101–200` @ Rs. 5/unit, `>200` @ Rs. 8/unit).
- Adds a fixed meter charge of Rs. 50 and applies a 10% rebate (`<= 80` units) or 15% surcharge (`> 300` units).
- Flags unusual spikes when a bill rises by more than 30% over the previous month.
- Displays a monthly summary and total payable amount.

## Algorithm
1. Start the program.
2. Read the number of months to evaluate.
3. Initialize empty lists for units and bills.
4. Loop through each month and read units consumed.
5. Skip the month if units are negative; otherwise compute slab-wise charges.
6. Add the fixed Rs. 50 charge and apply the rebate or surcharge.
7. Append the units and rounded bill to their respective lists.
8. Display each month's summary and alert if a bill exceeds 130% of the previous month's bill.
9. Display the total amount payable.
10. Stop the program.

## Sample Output
```text
Enter number of months: 3
Enter units consumed in Month 1: 75
Enter units consumed in Month 2: 150
Enter units consumed in Month 3: 320

----- ELECTRICITY BILL SUMMARY -----
Month 1: Units = 75.0 | Bill = Rs. 247.5
Month 2: Units = 150.0 | Bill = Rs. 600.0
  -> ALERT: Unusual spike compared to Month 1!
Month 3: Units = 320.0 | Bill = Rs. 2081.5
  -> ALERT: Unusual spike compared to Month 2!
Total Amount Payable: Rs. 2929.0
