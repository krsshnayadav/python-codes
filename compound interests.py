
principal=float(input("enter the principal amount="))
rate=float(input("enter the rate of interest="))
time=float(input("enter the time in years="))
CI=(principal*(1+(rate/100))**time)-principal
print(f"Compound interest on principal amount of {principal} is=",CI)
FINAL_AMOUNT =(principal + CI)
print(f"final amount of principal amount of {principal} is=",FINAL_AMOUNT)
per_month=(FINAL_AMOUNT/(time*12))
installments=(time*12)
print("you have to pay the final amount of %d rs. by paying  %d rs. per month till %d months"% (FINAL_AMOUNT,per_month,installments))

