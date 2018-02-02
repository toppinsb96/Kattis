import math

def convertToSeconds(time):
    return time[2] + time[1]*60 + time[0]*60*60

def difference(curr, exp):
    if(curr >= exp):
        exp += 86400
    return exp - curr

def secondsToFormat(time):
    hours = 0
    minutes = 0
    while(time >= 60 * 60):
        hours += 1
        time -= 60*60
    while(time >= 60):
        minutes += 1
        time -= 60

    print("%02d:%02d:%02d" % (hours,minutes,time))

current   = list(map(int, input().strip().split(":")))
explosion = list(map(int, input().strip().split(":")))
secondsToFormat(difference(convertToSeconds(current), convertToSeconds(explosion)))
