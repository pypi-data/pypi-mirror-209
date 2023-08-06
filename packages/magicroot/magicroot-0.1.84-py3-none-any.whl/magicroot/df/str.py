

def words(s):
    """
    Get all words in column of strings

    :Parameters:
        s : pandas.Series
            series of string values to get the words of

    :Returns:
        pandas.Series
            The Dataframe with one word per line
    """
    return s.drop_duplicates().str.split().explode().drop_duplicates().reset_index(drop=True)

