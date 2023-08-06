import pandas as pd
from datetime import date, timedelta
import holidays
import numpy as np


def perc(of, starting_on, ending_on, shift=1, upper=None, lower=None):
    starting_on = starting_on - pd.to_timedelta(shift, unit='D')
    p = (of - starting_on).dt.days / (ending_on - starting_on).dt.days
    return p.clip(upper=upper, lower=lower)


def shift(data, shift, unit):
    data, shift = pd.Series(data), pd.Series(shift)
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

    return rv if len(rv) > 1 else rv.iloc[0]


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


def periods_by(on, by, ouput_col='Values'):
    df = pd.concat([
        pd.DataFrame({ouput_col: on}).assign(Added=False),
        pd.DataFrame({ouput_col: by}).assign(Added=True, Period=lambda x: np.arange(x.shape[0]))
    ])
    df = df.sort_values([ouput_col, 'Added']).fillna(method='bfill').assign(
        Period=lambda x: x['Period'].fillna(x['Period'].max() + 1)
    )
    df['Period'] = df['Period'].astype(int)
    return df[~df['Added']].drop(columns='Added')
