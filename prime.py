#prime numbers between y and x

try:
    x = int(input("Prime numbers between...\nx: "))
    y = int(input("y: "))
except:
    print("Please enter valid integers.")
    quit()

if x>=y:
    print("x must be greater than y.")
    quit()


factors = 0
prime_numbers = []
 
for i in range(x,y+1):
    for j in range(1,i+1):
        if i % j == 0:
            factors += 1
    if factors == 2:
        prime_numbers.append(i)
    factors = 0

if not prime_numbers:
    print(f"There are no prime numbers between {x} and {y}.")
else:
    for i in prime_numbers:
        print(i, end = " ")
    print()