# gcd.py

def greatest_common_den(n1, n2):
    gcd_found = 0
    if n1 == n2:
        gcd_found = n1
    else:
        if n1 < n2:
            gcd_found = greatest_common_den(n1, n2 - n1)
        else:
            gcd_found = greatest_common_den(n1 - n2, n2)
    return gcd_found




num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

if num1 < 1 or num2 < 1:
    print('Note: neither value can be less than 1')
else:
    gcd = greatest_common_den(num1, num2)

print('The greatest common denominator for %d and %d is ' % (num1, num2), end='')
print(gcd)

