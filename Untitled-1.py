def interest (principal, rate, time):
    interest = (principal * rate * time)/100
    return interest

cal_interest = interest(10,3,2)
print (f"Interest is {cal_interest}")