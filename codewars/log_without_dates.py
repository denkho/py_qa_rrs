# https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6/

def to_secs(t):
    """Trasfer time from log str format hh:mm:ss to int format of seconds"""
    time_full = list(map(int, t.split(':')))
    return time_full[0] * 3600 + time_full[1] * 60 + time_full[2]

def check_logs(log):
    """Count of days in logs"""
    if len(log) == 0:
        return 0
    if len(log) == 1:
        return 1
    days = 1
    # time_start is a time to start counting the number of seconds in the log
    for i in range(1, len(log)):
        if to_secs(log[i]) <= to_secs(log[i - 1]):
            days += 1
    return days


# def check_logs(log):
#     last = [24, 0, 0]
#     days = 0
#     for t in log:
#         ts = list(map(int, t.split(':')))
#         if ts <= last: days += 1
#         last = ts
#     return days

print(check_logs(["12:12:12"]))  # 1
print(check_logs(["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"])) # 1
print(check_logs(["12:00:00", "23:59:59", "00:00:00"])) # 2
print(check_logs(["12:00:00", "12:00:00", "00:00:00"])) # 3
