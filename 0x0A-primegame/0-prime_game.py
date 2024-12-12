primeCheck = int(input("Enter a number: "))

if primeCheck <= 1:
    print("Not a prime number")  
else:
    is_prime = True  
    for i in range(2, int(primeCheck ** 0.5) + 1):
           if primeCheck % i == 0:
            is_prime = False  
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")

