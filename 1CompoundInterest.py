#interest= balance x monthly rate 
#new balance = balance + interest + contributions 
#Input your own balance, rates , contributions, years

balance = float(input("Starting Balance: "))
annual_rate = float(input("Annual Interest Rate(%): "))
contributions = float(input("Monthly Contributions: "))
years = int(input("Years: "))

annual_rate_adjusted = annual_rate / 100
yearly_contributions = contributions * 12 

for i in range(1, years +1):#+1 means years increment of +1
    interest = balance * annual_rate_adjusted
    balance = balance + interest + yearly_contributions
    #f-string drop variables inside{}
    #The :.2f shows a flaot with 2 decimal places 
    print(f"Year {i}: Interest ${interest:.2f}, Cumulative Balance ${balance:.2f}")
    #print i because i is the loop


    #next idea is to add a total contributions 
