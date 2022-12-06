#Let the given two dates be "1-Feb-2000" and "1-Feb-2004"
#dt1 = {1, 2, 2000};
#dt2 = {1, 2, 2004};
#Count number of days before dt1. Let this count be n1.
#Every leap year adds one extra day (29 Feb) to total days.
#n1 = 2000*365 + 31 + 1 + Number of leap years 
#Count of leap years for a date 'd/m/y' can be calculated 
#using the following formula:
#Number leap years 
# = floor(y/4) - floor(y/100) + floor(y/400) if m > 2
#  = floor((y-1)/4) - floor((y-1)/100) + floor((y-1)/400) if m <= 2
#All above divisions must be done using integer arithmetic
#So that the remainder is ignored.
#For 01/01/2000, leap year count is 1999/4 - 1999/100 
#+ 1999/400 which is 499 - 19 + 4 = 484
#Therefore n1 is 2000*365 + 31 + 1 + 484
#
#Similarly, the count number of days before dt2. 
#Let this the count be n2.Finally, return n2-n1
#This program is to find the number of days he/she lived:

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def countLeapYears(d):
    years = d.y
    if (d.m <= 2):
        years -= 1
    val = int(years / 4)
    val -= int(years / 100)
    val += int(years / 400)
    return val 
def getDifference(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
    n1 += countLeapYears(dt1)
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
    return (n2 - n1)
# asking input fron the user:
presentday=int(input("Enter present Day: "))
presentmonth=int(input("Enter present Month: "))
presentyear=int(input("Enter present Year: "))
day=int(input("Enter birth Day: "))
month=int(input("Enter birth Month: "))
year=int(input("Enter birth Year: "))
dt1 = Date(day, month, year)
dt2 = Date(presentday, presentmonth, presentyear)
# calling function:
print("Number of days you have survied is : ", getDifference(dt1, dt2))