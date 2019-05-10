import datetime


def now_subtracted_weeks(weeks):
    return datetime.datetime.today() - datetime.timedelta(weeks=weeks)


def now_formatted_subtracted_weeks(weeks):
    return now_subtracted_weeks(weeks=weeks).strftime('%d/%m/%Y')
