import datetime
from dateutil.parser import parse

__max_time_span = datetime.timedelta(days=90)
__zero_time_span = datetime.timedelta(days=0)


def get_comments(x, max_time_span=__max_time_span, zero_time_span=__zero_time_span):
    result = []

    time_span = datetime.timedelta(days=0)
    for y in eval(x[1]).values():
        for z in y:
            _span = x[0] - parse(z["referenceTime"])
            if _span > zero_time_span:
                if _span > max_time_span:
                    time_span = max_time_span
                    break
                elif _span > time_span:
                    time_span = _span

    time_ceiling = x[0] + time_span
    time_floor = x[0] - time_span
    for y in eval(x[1]).values():
        for z in y:
            if (
                parse(z["referenceTime"]) > time_floor
                and parse(z["referenceTime"]) < time_ceiling
            ):
                result.append((z["referenceTime"], z["score"], z["content"]))
    return result


def get_comments_(x, max_time_span=__max_time_span, zero_time_span=__zero_time_span):
    result = []
    time_span = datetime.timedelta(days=0)
    for y in eval(x[1]):
        _span = x[0] - parse(y["referenceTime"])
        if _span > zero_time_span:
            if _span > max_time_span:
                time_span = max_time_span
                break
            elif _span > time_span:
                time_span = _span

    time_ceiling = x[0] + time_span
    time_floor = x[0] - time_span
    for y in eval(x[1]):
        if (
            parse(y["referenceTime"]) > time_floor
            and parse(y["referenceTime"]) < time_ceiling
        ):
            result.append((y["referenceTime"], y["score"], y["content"]))
    return result


def deduplicate(x:list):
    x_=list(set(x))
    print(len(x),' to ',len(x_))
    return x_