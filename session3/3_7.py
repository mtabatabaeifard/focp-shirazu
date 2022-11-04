n = int(input("how many number?:"))
sum1 = 0
for i in range(n):
    new = int(input("next number:"))
    sum1 = sum1+new
print("sum:" , sum1 , "average:" , sum1/n)