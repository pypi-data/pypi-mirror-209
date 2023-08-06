from ..cp._tec import Propagate
import pandas as pd


def propagate(on, by, inplace=False, validate=None, **kwargs):
    return Propagate()(target=on, config=by, inplace=inplace, validate=validate, **kwargs)


def complete(target, with_cols_from, target_name='target', with_cols_from_name='with_cols_from'):
    common_cols = list(set(target.columns).intersection(set(with_cols_from.columns)))
    return target.merge(with_cols_from[common_cols].drop_duplicates(), how='outer', indicator=True).replace({
        'right_only': 'Not in ' + target_name, 'left_only': 'Not in ' + with_cols_from_name})




