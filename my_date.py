#######################################################
# my_date
#
# Name: VAMSHI KRISHNA THUME (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
print(is_leap_year(2020))
pass
 
def ordinal_date(year:int , month: int, day: int) -> int:
    # Individual days have been added upto end of the year in ordinal_dates
    ordinal_dates = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        ordinal_dates[2] = 60
    
    if month == 1:
        return day
    else:
        return ordinal_dates[month - 1] + day


print(ordinal_date(2023, 10, 28))

pass

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    
    ordinal_date1 = ordinal_date(year1, month1, day1)
    ordinal_date2 = ordinal_date(year2, month2, day2)
    ordinal_date_diff = abs(ordinal_date1 - ordinal_date2)
    year_diff = (year1 - year2) * 365
    ordinal_date_diff += year_diff
    
    leap_years_elapsed = 0

    def leap_year_elapsed(year1, year2):
        leap_years_elapsed = 0
        for y in range(year1, year2 + 1):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                leap_years_elapsed += 1
        return leap_years_elapsed
    leap_year_elapsed(year1,year2)

    return abs(ordinal_date_diff + leap_years_elapsed )

print(days_elapsed(2023, 10, 1, 2023, 5, 1))
    
pass

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        e = days_elapsed(2000,1,1,year,month,day)
        result = (e % 7) + 1

    else:
        e = days_elapsed(2000,1,1,year,month,day)
        result = (e % 7) 

    return DAYS_OF_WEEK[result]
    
print(day_of_week(2023,9,29))
pass
    
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    required_day = day_of_week(year, month, day)
    return f"{required_day}, {day:02d} {months[month - 1]} {year}"
pass

print(to_str(2023,9,29));
              
    