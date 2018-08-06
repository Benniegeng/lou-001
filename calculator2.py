#!/usr/bin/env python3
import sys
def tax_num(salary):
    a = salary - 3500 - salary * 0.165
    if a <= 0:
        tax = 0
    elif a <= 1500:
        tax = a * 0.03
    elif a <= 4500:
        tax = a * 0.1 - 105
    elif a <= 9000:
        tax = a * 0.2 - 555
    elif a <= 35000:
        tax = a * 0.25 - 1005
    elif a <= 55000:
        tax = a * 0.3 - 2775
    elif a <= 80000:
        tax = a * 0.35 - 5505
    else:
        tax = a * 0.45 - 13505
    return a + 3500 - tax
    
if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        try:
            num, salary = arg.split(':')
        except ValueError:
            print("Parameter Error")
            sys.exit()
        print('{}:{:.2f}'.format(num, tax_num(int(salary))))

