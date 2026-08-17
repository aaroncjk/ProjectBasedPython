#interest= balance x monthly rate 
#new balance = balance + interest + contributions 

balance = 1000
monthly_rate = 0.01
contributions = 100
months = 12

for month in range(1, months +1):
    interest = balance * monthly_rate
    balance = balance + interest + contributions
    #f-string drop variables inside{}
    #The :.2f shows a flaot with 2 decimal places 
    print(f"Month {month}: interest {interest:.2f}, balance ${balance:.2f}")