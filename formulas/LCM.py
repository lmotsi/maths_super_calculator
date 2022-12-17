#lowest common multiple between m and n
try:
    n = int(input("Lowest common multiple for...\nx: "))
    m = int(input("y: "))
except:
    print("Please enter valid integers.")
    quit()

x,y = n,m
b = [y]
a = [x]
LCM = 0
while True:
    x += n
    y += m
    b.append(y)
    a.append(x)
    if x in b:
        LCM = x;
        break
    if y in a:
        LCM = y
        break
    
print(f"Lowest common multiple is {LCM}")