import numpy as np
import pandas as pd
from . import create


def uniformize_columns(*args):
    """
    Created empty columns in the Dataframes, such that all Dataframes provided have the same columns
    :param args:
    :return:
    """
    columns = list({column for df in args for column in df.columns.to_list()})
    for column in columns:
        for df in args:
            if column not in df:
                df[column] = np.nan
    return (arg for arg in args)


def uniformize_index(index, *args):
    """
    Created empty rows in the Dataframes, such that all Dataframes provided have the same shape
    :param index:
    :param args:
    :return:
    """
    index_values = pd.concat([df[index] for df in args]).drop_duplicates().reset_index(drop=True)
    return (index_values.merge(df, how='left')[df.columns] for df in args)


def uniformize(index, *args):
    """
    Created empty rows and columns in the Dataframes, such that all Dataframes provided have the same shape
    :param index:
    :param args:
    :return:
    """
    return uniformize_index(index, *uniformize_columns(*args))


def uniformize_shape(*args):
    """
    Created empty rows and columns in the Dataframes, such that all Dataframes provided have the same shape
    :param args:
    :return:
    """
    args = uniformize_columns(*args)
    shape = np.maximum(*[df.shape for df in args])

    canvas = create.empty(shape, columns=args[0].columns)

    return (canvas.fillna(df) for df in args)

