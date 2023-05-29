def prime_number_checker(num):

    if num == 1:
        print(f'{num} is not a prime number!')

    elif num > 1:    
        # range between 2 and num - 1
        for i in range(2,num):
            #if num got a remainder with any number other than itself or 1 it is not a prime number
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f'{num} is a prime number')

for i in range(1,101):
    prime_number_checker(i)
