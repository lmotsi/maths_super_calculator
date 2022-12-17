#highest common factors of n and m
try:
    n = int(input("Highest common factor of... \nx: "))
    m = int(input("y: "))
except:
    print("Please enter valid numbers.")
    quit()
   
common_factor = 1
    
for i in range(1,max(n,m)+1):
    if n % i == 0 and m % i == 0:
        common_factor = i;
        
print(f"Highest common factor is {common_factor}")