#factors of n
try:
    n = int(input("Factors of: "))
except:
    print("Please enter valid numbers.")
    quit()
    
factors = []
for i in range(1,n+1):
    if n % i == 0:
        factors.append(i)

for i in factors:
    print(i, end = " ")
    
print()