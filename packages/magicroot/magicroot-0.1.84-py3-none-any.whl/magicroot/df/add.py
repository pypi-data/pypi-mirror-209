
def column_name(df, prefix: str = '', suffix='', to_columns=None):
    """
    Add sufixes and prefixes to many columns at once


    .. deprecated:: v0.0.2
                    to be moved to df.cols.

    :Parameters:
        df : pandas.Dataframe
            Dataframe to operate on
        prefix : str
            prefix to add
        suffix : str
            sufix to add
        to_columns : list
            list of columns to operate on

    :Returns:
        pandas.Dataframe
            The Dataframe with the names changed
    """
    if to_columns:
        df.columns = [prefix + column + suffix if column in to_columns else column for column in df.columns]
    return df
