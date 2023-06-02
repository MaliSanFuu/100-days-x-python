from calendar import month_name

def is_leap_year(year):
    """
    Check if a year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    """
    Get the number of days in a month for a given year.

    Args:
        year (int): The year.
        month (int): The month (1-12).

    Returns:
        tuple: A tuple containing the number of days in the month and the name of the month.
            If the month is invalid, returns ("Invalid month!", "").
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ]
    
    if month > 12 or month < 1:
        return "Invalid month!", ""
    elif is_leap_year(year) and month == 2:
        return month_days[month - 1] + 1, month_names[month - 1]
    else: 
        return month_days[month - 1], month_names[month - 1]

year = int(input("Enter a year: \n"))
month = int(input("Enter a month: \n"))

month_days, month_name = days_in_month(year, month)

if year > 2023:
    print(f'The {month_name} in {year} has {month_days} days!')
else:
    print(f'The {month_name} in {year} had {month_days} days!')
