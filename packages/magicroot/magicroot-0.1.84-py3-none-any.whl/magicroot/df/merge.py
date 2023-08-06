

def tagged(left, right, tag_col, left_tag='left_only', both_tag='both', right_tag='right_only', **kwargs):
    df = left.merge(right, **kwargs, indicator=tag_col)
    df[tag_col] = df[tag_col].replace({'left_only': left_tag, 'both': both_tag, 'right_only': right_tag})
    return df
