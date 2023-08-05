# -*- coding: utf-8 -*-

from datetime import datetime

def get_now_date(hyphen='',date=datetime.now()):
    # current_date = datetime.now().date()
    formatted_date = date.strftime(f"%Y{hyphen}%m{hyphen}%d")
    return formatted_date


def get_now_time(hyphen='',time=datetime.now()):
    # current_time = datetime.now().time()
    formatted_time = time.strftime(f"%H{hyphen}%M{hyphen}%S")
    return formatted_time


def get_now_datetime(hyphen_date='',hyphen_time='',hyphen_join='-',
                     date_time=datetime.now(),with_millison=False):
    # format=f"%Y{hyphen_date}%m{hyphen_date}%d{hyphen_join}%H{hyphen_time}%M{hyphen_time}%S"
    format=f"%Y{hyphen_date}%m{hyphen_date}%d{hyphen_join}"
    format=format+f"%H{hyphen_time}%M{hyphen_time}%S"
    # format = format + f"{hyphen_join}%f"[:3]

    # current_datetime = datetime.now()
    format_dt = date_time.strftime(format)

    if with_millison:
        milliseconds = str(date_time.microsecond)[:3].zfill(3)
        format_dt = format_dt+hyphen_join+milliseconds

    return format_dt

