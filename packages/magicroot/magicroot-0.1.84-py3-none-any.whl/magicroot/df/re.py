import regex as re


def classify(series, on_pattterns):
    df = series.to_frame('Original').assign(pat='')
    for pat in on_pattterns.drop_duplicates().astype(str):
        df = df.assign(
            pat=df['pat'].mask(df['Original'].astype(str).apply(lambda x: bool(re.fullmatch(pat, x))),
                                              pat)
        )
    return df['pat']
