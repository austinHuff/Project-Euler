# project euler 36
total = 0
for num in range(1,1000001):
    # first if checks if palindrome in decimal
    if str(num) == str(num)[::-1]:
        # palindrome in decimal now check binary
        if str(bin(num)[2:]) == str(bin(num)[2:])[::-1]:
            # palindrome in both, print both and add to total
            print(num)
            print(bin(num)[2:])
            total = total + num
        
print(total)
# produces correct solution, checked on website