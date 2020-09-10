import argparse
import sys
import math


def parser_setup(parser):
	parser.add_argument("--type", help = "indicates type of payment", type = str)
	parser.add_argument("--payment", help = "monthly payment", type = float)
	parser.add_argument("--principal", help = "initial credit", type = int)
	parser.add_argument("--periods", help = "number of months needed to repay credit", type = int)
	parser.add_argument("--interest", help = "interest rate in percentage", type = float)


def calc_diff_payments(P, i, n):
	sum_ = 0
	i = i / 12 / 100
	for m in range(1, n + 1):
		differentiated_payment = math.ceil(P / n + i * (P - (P * (m - 1) / n)))
		sum_ += differentiated_payment
		print(f"Month {m}: payment is {differentiated_payment}")
	overpayment = sum_ - P
	print(f"\nOverpayment = {overpayment}")

	
def calc_payment_amount(P, i, n):
	i = i / 12 / 100
	payment_amount = math.ceil(P * i * (1 + i) ** n / ((1 + i) ** n - 1))
	print(f"Your annuity payment = {payment_amount}!")
	overpayment = payment_amount * n - P
	print(f"Overpayment = {overpayment}")


def calc_credit_principal(A, i, n):
	i = i / 12 / 100
	credit_principal = round(A / (i * (1 + i) ** n / ((1 + i) ** n - 1)))
	print(f"Your credit principal = {credit_principal}!")
	overpayment = A * n - credit_principal
	print(f"Overpayment = {overpayment}")


def calc_num_periods(P, i, A):
    i = i / 12 / 100
    num_periods = math.ceil(math.log(A / (A - i * P), 1 + i))
    num_years = num_periods // 12
    num_months = num_periods % 12
    months_years_output = ""
    if num_years == 0:
        months_years_output = f"{num_months} month"
        if num_months > 1:
            months_years_output += "s"
    elif num_months == 0:
        months_years_output = f"{num_years} year"
        if num_years > 1:
            months_years_output += "s"
    else:
        months_years_output = f"{num_years} year"
        if num_years > 1:
            months_years_output += "s"
        months_years_output += f" {num_months} month"
        if num_months > 1:
            months_years_output += "s"

    print(f"It wil take {months_years_output} to repay this credit!")
    overpayment = A * num_periods - P
    print(f"Overpayment = {overpayment}")
    print(num_periods)
    print(math.log(A / (A - i * P), 1 + i))
	
	

def check_negatives(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return True
	else:
		return False


args = sys.argv
parser = argparse.ArgumentParser()
parser_setup(parser)
parse_args = parser.parse_args()
payment_type = parse_args.type
payment_amount = parse_args.payment
credit_principal = parse_args.principal
num_periods = parse_args.periods
credit_interest = parse_args.interest

if (len(args) != 5 or credit_interest == None):
	print("Incorrect parameters")
else:	
	if payment_type == "diff":
		if payment_amount != None or check_negatives(credit_principal, credit_interest, num_periods):
			print("Incorrect parameters")
		else:
			calc_diff_payments(credit_principal, credit_interest, num_periods)
	elif payment_type == "annuity":
		if payment_amount == None: # or check_negatives(credit_principal, num_periods, credit_interest):
			calc_payment_amount(credit_principal, credit_interest, num_periods)
		elif credit_principal == None:
			calc_credit_principal(payment_amount, credit_interest, num_periods)
		elif num_periods == None:
			calc_num_periods(credit_principal, credit_interest, payment_amount)
	else:
		print("Incorrect parameters")


  