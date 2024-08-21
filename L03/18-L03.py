def read_hour():
    hour = int(input('Enter hour: '))
    return hour
    
def read_minute():
    mins = int(input('Enter minute: '))
    return mins

def read_second():
    sec = int(input('Enter second: '))
    return sec

def to_seconds(h, m,s):
    return h*3600+m*60+s

def time_elapsed(start, finish):
    time_elapsed =  finish - start
    hour = time_elapsed // 3600 
    leftover = time_elapsed - (hour*3600)
    mins = leftover//60
    sec = leftover-(mins*60)
    return f'{hour} hours {mins} minutes {sec} seconds.'

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))