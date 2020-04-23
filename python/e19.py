"""
Counts the sundays between 1st Jan 1901 and 1st Jan 2001
"""
from datetime import date, timedelta
#date implements all the calendar generation.  This is easy...

def Euler_19():
    #verified
    start_date = date(1901, 1, 1)
    end_date = date(2001,1,1) #one extra to account for range()
    result = 0
    while (start_date < end_date):
        if (start_date.day == 1) and (start_date.isoweekday() == 7):
            result += 1
        start_date += timedelta(days = 1)
    return result

def test_19():
    assert Euler_19() == 171

if __name__ == "__main__":
    print(Euler_19())
