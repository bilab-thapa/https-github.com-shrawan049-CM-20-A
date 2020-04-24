N = int(input("Enter a number : "))
count = 1
for i in range(N):
    while (N>1):
        count *= N 
        N -= 1
print("The factorial is : ", count)