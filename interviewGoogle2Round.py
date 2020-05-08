# Given a file consisting of lines like this:
# 2017-02-01T20:00 OperationA Start
# 2017-02-01T20:01 OperationA End  … 1 min
# 2017-02-01T20:08 OperationB Start
# 2017-02-01T20:09 OperationC Start
# 2017-02-01T20:10 OperationB End … 2 Min
# 2017-02-01T20:12 OperationC End ..3 min
# 2017-02-01T20:09 OperationCCC Start

# Produce an average runtime of all operations.
# Example output:
# Average: 0 days 0 hours 2 minutes  (0 days 0 hours 6 minutes total for 3 operations)
from datetime import datetime,date,time, timezone
def break_line(oneline):
    info = oneline.split()
    operationCounter = 0
    difference = 0
    if info[2] == 'Start':
        operStartTime[info[1]] = info[0]
        operationCounter = 1

    if info[2] == 'End':
        #input 的時間格式: '2017-02-01T20:09' ->"%Y-%m-%dT%H:%M"
        startDateStr = datetime.strptime(operStartTime.get(info[1]), "%Y-%m-%dT%H:%M")
        endDateStr = datetime.strptime(info[0], "%Y-%m-%dT%H:%M")
        difference = endDateStr- startDateStr
        print(info[1], difference)
        # End-Start 後會有2種格式 1.時分秒 0:03:00 跟 2.日時分秒 1461 days, 1:00:00
        if 'days' in str(difference): # day + time
            datetimesplit = str(difference).split() #[0]:天數 [2]:時分秒

            timesplit = datetimesplit[2].split(':')
            timesplit[0], timesplit[1], timesplit[2] = int(timesplit[0]), int(timesplit[1]), int(timesplit[2])
            difference = int(datetimesplit[0])*1440+timesplit[0]*60 + timesplit[1]
        else: # time only
            timesplit = str(difference).split(':')
            timesplit[0], timesplit[1], timesplit[2] = int(timesplit[0]), int(timesplit[1]), int(timesplit[2])
            difference = timesplit[0]*60 + timesplit[1]
        del operStartTime[info[1]]
    return difference, operationCounter

def convert_Time(mins):
    days = mins // 1440 # 1 day 1440 mins
    hours = (mins - days * 1440) // 60 # 1hr 60 mins
    return days, hours, mins % 60

openLog= open('log.txt')
oneline = openLog.readline()
operStartTime = {}
totaltime = 0
totaloperation = 0
while oneline:
    onelinetime, onelineop = break_line(oneline)
    if onelineop == 0:
        totaltime = totaltime + onelinetime
    else:
        totaloperation = totaloperation+onelineop
    oneline = openLog.readline()
print()
dayA, hoursA, minA = convert_Time(totaltime//totaloperation)
dayB, hoursB, minB = convert_Time(totaltime)
print('Average:',dayA,'days',hoursA,'hours',minA,'minutes')
print('Total:',dayB,'days',hoursB,'hours',minB,'minutes total for',totaloperation,'operations')