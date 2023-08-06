"""
This file contains the functions used to compute useful values for predetermined dataframe structures
"""
from . import format
from datetime import timedelta
import numpy as np
import pandas as pd


def duration(df, dt_begin, dt_end, computed_column='duration', days=False,  *args, **kwargs):
    """
    Computes duration in days between two dates
    :param df: Dataframe
        :column dt_begin: column(s) should be in the table
        :column dt_end: column(s) should be in the table
    base to compute

    :param dt_begin: str
    column with the begin date

    :param dt_end: str
    column with the end date

    :param computed_column: str, default 'maturity'
    column with the name to give to the column with the computed duration

    :return: Dataframe
        :column previous: all column(s) previously in the table
        :column duration_column: computed column
    result table
    """
    multiplier = 1 if days else 365
    return format.as_date(df, [dt_begin, dt_end], *args, **kwargs).assign(
        **{
            computed_column: lambda x: np.maximum((x[dt_end] - x[dt_begin]).dt.days / multiplier, 0)
        }
    )


def date_perc(df, dt_begin, dt_end, dt_ref, duration_column='duration_pct',  *args, **kwargs):
    """
    Computes percentage of a date between to ZZ_other dates
    :param df: Dataframe
        :column dt_begin: column(s) should be in the table
        :column dt_end: column(s) should be in the table
    base to compute

    :param dt_begin: str
    column with the begin date

    :param dt_end: str
    column with the end date

    :param dt_ref: str
    column with the end date

    :param duration_column: str, default 'maturity'
    column with the name to give to the column with the computed duration

    :return: Dataframe
        :column previous: all column(s) previously in the table
        :column duration_column: computed column
    result table
    """
    return format.as_date(df, [dt_begin, dt_end, dt_ref], *args, **kwargs).assign(
        **{
            duration_column: lambda x:
            duration(x, dt_begin, dt_ref)['duration'] / duration(x, dt_begin, dt_end)['duration']
        }
    )


def maturity(begin_date, end_date):
    """
    Computes maturity
    :param begin_date: str
    Series with the begin date

    :param end_date: str
    Series with the end date

    :return: func to be applied to a Dataframe
    """
    return (end_date - begin_date).where(end_date > begin_date, timedelta(days=0))


def discount_rate(with_rate, with_maturity, days_in_year=365):
    """
    Computes discount rate

    :param with_rate: str
    Series with the spot rate

    :param with_maturity: str
    Series with the maturity

    :param days_in_year: int
    constant with the days in the year

    :return: func to be applied to a Dataframe
    """
    return lambda x: 1 / (1 + with_rate).pow(with_maturity.dt.days / days_in_year)


def discounted_cashflows(df, cashflow_columns, disc_rate_column, prefix='disc_', suffix=''):
    """
    Discounts cashflows
    :param df: Dataframe
        :column cashflow_columns: column(s) should be in the table
        :column disc_rate_column: column(s) should be in the table
    base to compute

    :param cashflow_columns: list
    containing columns with cashflows to discount

    :param disc_rate_column: str
    Column with the discount rate

    :param prefix: str, default 'disc_'
    column with the prefix to add to the column names with the discounted cashflows

    :param suffix: str, default ''
    column with the suffix to add to the column names with the discounted cashflows

    :return: Dataframe
        :column previous: all column(s) previously in the table
        :column prefix + cashflow_columns: computed columns
    result table
    """
    return df.assign(
        **{
            prefix + column + suffix: df[column] * df[disc_rate_column]
            for column in cashflow_columns
        }
    )


def discounted_columns_pairs(cashflow_columns, prefix, suffix):
    """
    Computes a dictionary with the undiscounted version of columns as keys and the discounted version as values

    :param cashflow_columns: list
    undiscounted cashflow columns

    :param prefix: str
    prefix used to mark discounted columns

    :param suffix: str
     prefix used to mark discounted columns

    :return: a dictionary with the undiscounted version of columns as keys and the discounted version as values
    """
    return {
        undiscounted_column: prefix + undiscounted_column + suffix for undiscounted_column in cashflow_columns
    }


def discounted_components(df, cashflow_columns, prefix='comp_', suffix=''):
    """
    Computes discounted amounts from cashflows
    :param df: Dataframe
        :column cashflow_columns: column(s) should be in the table
    base to compute

    :param cashflow_columns: list
    containing columns with cashflows to discount

    :param prefix: str, default 'comp_'
    column with the prefix to add to the column names with the discounted amounts from cashflows

    :param suffix: str, default ''
    column with the suffix to add to the column names with the discounted cashflows

    :return: Dataframe
        :column previous: all column(s) previously in the table
        :column prefix + cashflow_columns: computed columns
    result table
    """
    return df.assign(
        **{
            prefix + disc_cashflow_column + suffix: lambda x: x[disc_cashflow_column] - x[cashflow_column]
            for cashflow_column, disc_cashflow_column in cashflow_columns.items()
        }
    )


def intersection_days(*args, shift_days=0):
    """
    Computes the intersection days between all given time windows
    All windows should be provided in the format ('begin column', 'end column')
    :return:
    """
    return lambda df: np.minimum(
                *[df[window[1]] for window in args]
            ) - np.maximum(
                *[df[window[0]] for window in args]
            ) + timedelta(days=shift_days)


def union_days(*args, shift_days=0):
    """
    Computes the union days between all given time windows
    All windows should be provided in the format ('begin column', 'end column')
    :return:
    """
    return lambda df: np.maximum(
                *[df[window[1]] for window in args]
            ) - np.minimum(
                *[df[window[0]] for window in args]
            ) + timedelta(days=shift_days)


def intersection_days_perc(*args, shift_days=0):
    """
    Computes the intersection days percentage between all given time windows
    All windows should be provided in the format ('begin column', 'end column')
    :return:
    """
    return lambda df: intersection_days(*args, shift_days=shift_days)(df) / union_days(*args, shift_days=shift_days)(df)


def eom(df, columns=None, prefix='eom_', suffix='', *args, **kwargs):
    return format.as_date(df, columns, *args, **kwargs).assign(
        **{
            prefix + column + suffix: lambda x: (x[column] - pd.to_timedelta(1, unit='day')) + pd.offsets.MonthEnd()
            for column in columns
        }
    )


