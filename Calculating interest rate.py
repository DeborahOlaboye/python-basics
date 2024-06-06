#Calculating interest rate
def interest (principal, rate, time_in_years, a = 100):
    interest = (principal * rate * time_in_years)/a
    principal = int()
    rate = int()
    if type(principal) != int:
        print("Value must be an integer")
    for time_in_years in range(1,12):
        time_in_months = time_in_years*12
    return interest

cal_interest = interest(10,3,8)
print (f"Interest is {cal_interest}")