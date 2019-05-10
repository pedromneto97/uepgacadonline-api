import datetime


def now_subtracted_weeks(weeks):
    return datetime.datetime.now() - datetime.timedelta(weeks=weeks)


def now_formatted_subtracted_weeks(weeks):
    return datetime.datetime.strptime(now_subtracted_weeks(weeks=weeks), '%d/%m/%Y')
