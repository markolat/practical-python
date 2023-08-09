# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
counter = 1

extra_payment_start_month = int(input("Extra payment start month (integer):"))
extra_payment_end_month = int(input("Extra payment end month (integer):"))
extra_payment = int(input("Extra payment amount (integer):"))

while principal > 0:
    if counter == extra_payment_start_month:
        payment += extra_payment
    if counter == extra_payment_end_month:
        payment -= extra_payment

    principal = principal * (1+rate/12) - payment
    if principal < payment:
        payment = principal
        principal = 0
    total_paid = total_paid + payment

    print(counter, round(total_paid, 2), round(principal, 2))
    counter += 1

print('Total paid', total_paid)
