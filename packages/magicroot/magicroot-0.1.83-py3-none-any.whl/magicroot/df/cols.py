

def without(df, columns):
    return [col for col in df.columns if col not in columns]


def common(df, df_other):
    return [col for col in df.columns if col in df_other.columns]


def split(df, all_except, value_name='value', sep='_', **kwargs):
    return df.melt(
        id_vars=all_except, value_name=value_name, var_name='col_names'
    ).assign(**kwargs).drop(columns=value_name).melt(
        id_vars=all_except + ['col_names'], value_name='split', var_name='variable'
    ).assign(col_names=lambda x: x['col_names'] + sep + x['variable']).pivot(
        index=all_except,
        columns='col_names',
        values='split'
    ).reset_index()


