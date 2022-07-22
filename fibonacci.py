try:
    n = int(input("Fibonacci sequence until: "))
except:
    print("Please enter a valid number.")
    quit()
    
i = 1
sums = 0
sequence = [0,1]
sums = 1
while sums<=n:
    sequence.append(sums)
    sums = sequence[i] + sequence[i+1]
    i = i+1

for i in sequence:
    print(i, end = " ")
print()
