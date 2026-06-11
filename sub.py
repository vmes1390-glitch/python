def sum(n):
    z=0
    for i in range(n):
        z+=i+1
    
    return z


x=int(input("Enter a number: "))

print(sum(x))