# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 49
extra_payment_end_month = extra_payment_start_month + 4*12
extra_payment = 1000

while principal > 0:
    month = month + 1
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        extraPmt = extra_payment
    else:
        extraPmt = 0.0
    if principal * (1+rate/12) - payment - extraPmt < 0:
        if principal * (1+rate/12) - payment < 0:
            payment =  principal * (1+rate/12)
            extraPmt = 0
        else: # ExtraPmt puts it over
            extraPmt = principal * (1+rate/12) - payment
    principal = principal * (1+rate/12) - payment - extraPmt
    total_paid = total_paid + payment + extraPmt
    print(f'Month: {month} Total Paid:  ${total_paid:0.2f} Remaining: ${principal:0.2f}')

print('Total Paid', total_paid)
print('Total Months', month)
