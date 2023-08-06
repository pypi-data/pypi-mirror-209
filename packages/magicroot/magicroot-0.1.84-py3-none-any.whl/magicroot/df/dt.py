import pandas as pd
from datetime import date, timedelta
import holidays
import numpy as np
from . import gen


def perc(of, starting_on, ending_on, shift=1, upper=None, lower=None):
    starting_on = starting_on - pd.to_timedelta(shift, unit='D')
    p = (of - starting_on).dt.days / (ending_on - starting_on).dt.days
    return p.clip(upper=upper, lower=lower)


def shift(data, shift, unit):
    data, shift = gen.coupled_series(data, shift)
    if unit.upper() == 'Y':
        rv = pd.to_datetime(
            (data.dt.year + shift).astype(str) + data.dt.month.astype(str) + data.dt.day.astype(str),
            format='%Y%m%d')
    elif unit.upper() == 'M':
        rv = pd.to_datetime(
            (data.dt.month + shift).astype(str) + data.dt.year.astype(str) + data.dt.day.astype(str),
            format='%m%Y%d')
    else:
        raise NotImplementedError(f'Cannot date shift with arguments of types '
                                  f'{type(data)=}, {type(shift)=}, {type(unit)=}')

    return rv


def mondays(start_dt, end_dt):  # January 1st
    d = start_dt + timedelta(days=6 - start_dt.weekday())  # First Sunday
    d += timedelta(days=1)  # make it monday
    while d < end_dt:
        yield d
        d += timedelta(days=7)


def specific_weekday(weekday, from_dt, to_dt):  # January 1st
    d = from_dt + timedelta(days=6 - from_dt.weekday())  # First Sunday
    d += timedelta(days=weekday - 1)  # make it monday
    while d < to_dt:
        yield d
        d += timedelta(days=7)


def portugal_holidays(start_date, end_date):
    # Get holidays for Portugal
    portugal_holidays = holidays.Portugal()

    # Iterate through all dates between start and end dates
    current_date = start_date
    while current_date <= end_date:
        # Check if current date is a holiday in Portugal
        if current_date in portugal_holidays:
            yield current_date, portugal_holidays[current_date]
        current_date += timedelta(days=1)


def periods(by, on):
    return lambda df: df.merge(pd.concat([
        df[[on]].drop_duplicates().assign(Added=False),
        by.drop_duplicates().frame(on).assign(Added=True, mr_dt_Aux_Period=gen.counting_col())
    ]).sort_values([on, 'Added']).fillna(method='bfill').assign(
        mr_dt_Aux_Period=lambda x: x['mr_dt_Aux_Period'].fillna(x['mr_dt_Aux_Period'].max() + 1).astype(int)
    ).loc[lambda x: ~x['Added']], how='left', validate='m:1', on=on)['mr_dt_Aux_Period']
