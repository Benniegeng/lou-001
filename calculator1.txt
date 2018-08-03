#!/usr/bin/env python3
import sys
try:
        a = int(sys.argv[1])
except ValueError:
        print("Parameter Error")
        sys.exit()
if a < 0:
        print('wrong')
        exit()
a -= 3500

if a <= 0:
        tax = 0
elif a <= 1500:
        tax = a * 0.03
elif a <= 5000:
        tax = a * 0.1 - 105
elif a <= 8000:
        tax = a * 0.2 - 555
elif a <= 12500:
        tax = a * 0.25 - 1005
elif a <= 38500:
        tax = a * 0.3 - 2775
elif a <= 58500:
        tax = a * 0.35 - 5505
else:
        tax = a * 0.45 - 13505
print('{.2f}'.format(int(tax)))
