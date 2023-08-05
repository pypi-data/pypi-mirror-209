import datetime

def _format_dt(dt: datetime.datetime) -> str:
    if dt:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return ""

def format_time_cost(seconds: float) -> str:
    SEC_PER_M = 60
    SEC_PER_H = 60 * 60
    SEC_PER_D = 60 * 60 * 24

    if seconds < 0:
        seconds = 0

    DAY = int(seconds // SEC_PER_D)
    HOUR = int((seconds - (DAY * SEC_PER_D)) // SEC_PER_H)
    MINUTE = int((seconds - (DAY * SEC_PER_D + HOUR * SEC_PER_H)) // SEC_PER_M)
    SECOND = seconds - (DAY * SEC_PER_D + HOUR * SEC_PER_H + MINUTE * SEC_PER_M)
    MSECOND = int((SECOND - int(SECOND))*1000)
    SECOND = int(SECOND)

    if DAY > 0:
        return '({}d {}h {}m {}s {}ms)'.format(DAY, HOUR, MINUTE, SECOND, MSECOND)
    if HOUR > 0:
        return '({}h {}m {}s {}ms)'.format(HOUR, MINUTE, SECOND, MSECOND)
    if MINUTE > 0:
        return '({}m {}s {}ms)'.format(MINUTE, SECOND, MSECOND)
    if SECOND > 0:
        return '({}s {}ms)'.format(SECOND, MSECOND)

    return '({}ms)'.format(MSECOND)
