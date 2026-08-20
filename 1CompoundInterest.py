#interest = balance x rate
#new balance = balance + interest + contributions
#Input your own balance, rates, contributions, years
while True:
   try:
       starting_balance = float(input("Initial Investment($): "))
       annual_rate = float(input("Annual Interest Rate(%): "))
       contributions = float(input("Monthly Contributions($): "))
       years = int(input("Years: "))
   except ValueError:
       print("Invalid input. Please enter numeric values.")
       continue

   if starting_balance < 0 or annual_rate < 0 or contributions < 0 or years <= 0:
       print("Invalid Input. Please enter positive values.")
       continue
   else:
       break

annual_rate_adjusted = annual_rate / 100
yearly_contributions = contributions * 12
balance = starting_balance      # working copy the loop is allowed to overwrite

for i in range(1, years + 1):   # range stops before the end value, so +1 includes the final year
    interest = balance * annual_rate_adjusted
    total_contributions = yearly_contributions * i
    balance = balance + interest + yearly_contributions

    print(f"Year {i}: Interest ${interest:.2f}, Cumulative Balance ${balance:.2f}")

total_contributions = yearly_contributions * years
total_interest = balance - starting_balance - total_contributions

print(f"Initial Investment: ${starting_balance:.2f}")
print(f"Total Contributions: ${total_contributions:.2f}")
print(f"Total Interest: ${total_interest:.2f}")
print(f"Final Balance: ${balance:.2f}")
# this is basically the summary of after the total(i) years of compounding. I would add a graph of the compound effect


#include libraries pip3 install matplotlib
import matpotlib.pylot as plt
