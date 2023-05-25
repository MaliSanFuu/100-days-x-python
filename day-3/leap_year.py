year = int(input("Input the year you want to check: \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(
                f"{year} is not a leap year because it is not cleanly divisible by 400"
            )
    else:
        print(f"{year} is  a leap year")
else:
    print(f"{year} is not a leap year because it is not cleanly divisible by 4")