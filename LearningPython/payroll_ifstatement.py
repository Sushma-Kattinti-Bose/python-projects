import sys


def payroll_rate():

    print("Enter Hours worked")
    hoursWorked = int(input())
    rate = 25.00
    if hoursWorked > 40:
        grossPay = (40 * rate) + (hoursWorked - 40) * (rate * 1.5)
    # if hoursWorked <= 40:
    else:
        grossPay = hoursWorked * rate
    print("Gross Pay:" + str(grossPay))

if __name__ == "__main__":
    payroll_rate()
    