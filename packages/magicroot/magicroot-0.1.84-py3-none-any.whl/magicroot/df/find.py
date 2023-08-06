import pandas as pd
from fuzzywuzzy import process


def best_matches(phrase, on, n=5):
    return process.extract(query=phrase, choices=on, limit=n)
    # matches = process.extract(phrase, on)
    # log.debug(f'Searched \'{self.path}\' for \'{key.root}\' and found {matches.__str__()}')
    # match_path = os.path.join(self.path, matches[0][0])
    # folder = Navigator(match_path)
    # if len(key) > 1:
    #     log.debug(f'Will continue search algoritm: Since \'{key}\' has lenght {len(key)}')
    #     return folder.search(key.without_root)
    # log.debug(f'Concluded search algoritm: Since \'{key}\' has lenght {len(key)}')
    # return folder


def classify(phrase, on, with_detail=False):
    matches = process.extract(query=phrase, choices=on, limit=len(on))
    df = pd.DataFrame.from_records(matches, columns=['word', 'score', 'index'])
    if with_detail:
        return df
    return on.to_frame('word').merge(df, how='left', validate='m:1')['score']



