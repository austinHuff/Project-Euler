import math

# project euler problem 125

total = 0
for num in range(1,100000001):
    # first if checks if palindrome in decimal
    if str(num) == str(num)[::-1]:
        print("NUM-----" ,num)
        for i in range(1,int(math.sqrt(num))):
            testSum = 0
            j = i+1
            while i <= j <= math.sqrt(num):
                k = j
                testB = True
                #print("for j=" , j)
                while k < int(math.sqrt(num)) & testB == True:
                    #print("while k=",k)
                    testSum += (k**2)
                    if testSum < num:
                        k = k +1
                    if testSum == num:
                        total += num
                        testB = False
                        j = math.sqrt(num) + 500
                    if testSum > math.sqrt(num):
                        k = 1000000000000
                
        
print("Total" , total)
