# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
# year- 31536000 day- 86400 hour- 3600

def format_duration(seconds):
    if seconds == 0:
        return 'now'

    years = seconds // 31536000
    seconds = seconds - years * 31536000
    days = seconds // 86400
    seconds = seconds - days * 86400
    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60

    res = []
    if years > 0:
        if years > 1:
            res_years = f'{years} years'
            res.append(res_years)
        if years == 1:
            res_years = f'{years} year'
            res.append(res_years)

    if days > 0:
        if days > 1:
            res_days = f'{days} days'
            res.append(res_days)
        if days == 1:
            res_days = f'{days} day'
            res.append(res_days)

    if hours > 0:
        if hours > 1:
            res_hours = f'{hours} hours'
            res.append(res_hours)
        if hours == 1:
            res_hours = f'{hours} hour'
            res.append(res_hours)

    if minutes > 0:
        if minutes > 1:
            res_minutes = f'{minutes} minutes'
            res.append(res_minutes)
        if minutes == 1:
            res_minutes = f'{minutes} minute'
            res.append(res_minutes)

    if seconds > 0:
        if seconds > 1:
            res_seconds = f'{seconds} seconds'
            res.append(res_seconds)
        if seconds == 1:
            res_seconds = f'{seconds} second'
            res.append(res_seconds)


    if len(res) == 5:
        return f'{res[0]}, {res[1]}, {res[2]}, {res[3]} and {res[4]}'

    if len(res) == 4:
        return f'{res[0]}, {res[1]}, {res[2]} and {res[3]}'

    if len(res) == 3:
        return f'{res[0]}, {res[1]} and {res[2]}'

    if len(res) == 2:
        return f'{res[0]} and {res[1]}'

    if len(res) == 1:
        return f'{res[0]}'







print(format_duration(63))