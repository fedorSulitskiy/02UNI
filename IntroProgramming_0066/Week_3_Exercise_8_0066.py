# 8
import datetime as dt
startDate = dt.datetime(2025, 4, 27)
endDate = dt.datetime(2025, 5, 7)

def exercise_8(startDate, endDate):
    import datetime as dt
    endDate = dt.datetime(2025, 5, 7)

    while endDate >= startDate:
        yield startDate
        startDate += dt.timedelta(days=1)

test = exercise_8(startDate, endDate)
for i in range((endDate - startDate).days+1):
    print(next(test).date())