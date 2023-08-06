from ._component import Component


class Forward(Component):
    def run(self, quotes, forward, col_rate='QUOTE_RT', col_mat='MATURITY_DT'):
        if isinstance(forward, int):
            quotes['FORWARD'] = forward

        fwr_quotes = quotes.merge(quotes.rename(columns={col_rate: 'QUOTE_FWR_DEN'}).assign(
                MATURITY_DT=lambda x: x[col_mat] - quotes['FORWARD']
        ), how='left')
        quotes = fwr_quotes.merge(quotes.rename(columns={col_rate: 'QUOTE_FWR_NUM'}).assign(
            MATURITY_DT=lambda x: x[col_mat] - quotes['FORWARD'] + 1
        ), how='left')

        quotes[col_rate] = \
            (
                    (1 + quotes['QUOTE_FWR_NUM']) ** (quotes['FORWARD'] + 1) /
                    (1 + quotes['QUOTE_FWR_DEN']) ** quotes['FORWARD']
            ).fillna((1 + quotes['QUOTE_FWR_NUM']) ** (quotes['FORWARD'] + 1)) - 1
        quotes = quotes.drop(columns=['QUOTE_FWR_DEN', 'QUOTE_FWR_NUM'])
        quotes = quotes.sort_values(
            [col for col in quotes.columns if col not in [col_mat, 'FORWARD', col_rate]] + [col_mat]
        ).fillna(method='ffill')
        return quotes


class ForwardMonth(Component):
    def run(self, quotes, forward, col_rate='QUOTE_RT', col_mat='MATURITY_DT'):
        # if isinstance(forward, int):
        #     quotes['FORWARD'] = forward

        fwr_quotes = quotes.merge(quotes.rename(columns={col_rate: 'QUOTE_FWR_DEN'}).assign(
                MATURITY_DT=lambda x: x[col_mat] - quotes['FORWARD']
        ), how='left')
        quotes = fwr_quotes.merge(quotes.rename(columns={col_rate: 'QUOTE_FWR_NUM'}).assign(
            MATURITY_DT=lambda x: x[col_mat] - quotes['FORWARD'] + 1
        ), how='left')

        quotes[col_rate] = \
            (
                    (1 + quotes['QUOTE_FWR_NUM']) ** (quotes['FORWARD'] + 0.0849315068493151) /
                    (1 + quotes['QUOTE_FWR_DEN']) ** quotes['FORWARD']
            ).fillna((1 + quotes['QUOTE_FWR_NUM']) ** (quotes['FORWARD'] + 0.0849315068493151)) - 1
        quotes = quotes.drop(columns=['QUOTE_FWR_DEN', 'QUOTE_FWR_NUM'])
        quotes = quotes.sort_values(
            [col for col in quotes.columns if col not in [col_mat, 'FORWARD', col_rate]] + [col_mat]
        ).fillna(method='ffill')
        return quotes
