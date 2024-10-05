import random
import time
def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and",endDate)    
    RandomGenerator= random.random()
    dateFormat= '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = starttime + RandomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("random date = ", getRandomDate("5/25/2022", "02/19/2026"))


