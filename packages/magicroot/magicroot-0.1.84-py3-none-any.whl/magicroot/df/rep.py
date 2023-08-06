

def common_columns(left, right):
    """

    .. deprecated:: v0.0.2
                    to be moved to :py:func:`magicroot.df.cols.common`.

    """
    return [col for col in left.columns if col in right.columns]


def common_lines(left, right, names=('left', 'right'), col_name='In_Table'):
    common_cols = common_columns(left, right)
    df = left[common_cols].drop_duplicates().merge(
        right[common_cols].drop_duplicates(), how='outer', indicator=col_name)
    df[col_name] = df[col_name].str.replace('left', names[0]).str.replace('right', names[1])
    return df


