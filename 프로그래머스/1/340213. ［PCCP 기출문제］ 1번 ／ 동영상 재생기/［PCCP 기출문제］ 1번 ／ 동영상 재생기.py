'''
[기본]
처음 : 0분 0초
[기능]
- 10초 전으로
    10초 미만이면 처음으로
    
- 10초 후로
    남은 시간이 10초 미만이면 맨 끝으로(동영상의 길이)
- 오프닝 건너뛰기
    



'''

def time_to_minute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute
def minute_to_time(minutes):
    hour = str(minutes//60)
    minute = str(minutes%60)
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    return f"{hour}:{minute}"

def solution(video_len, pos, op_start, op_end, commands):
    
    pos = time_to_minute(pos)
    video_len = time_to_minute(video_len)
    op_start = time_to_minute(op_start)
    op_end = time_to_minute(op_end)
    
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == 'next':
            if pos + 10 >= video_len:
                pos = video_len
            else:
                pos += 10
        elif command == 'prev':
            if pos - 10 <= 0:
                pos = 0
            else:
                pos -= 10
                
    if op_start <= pos <= op_end:
        pos = op_end
    return minute_to_time(pos)