from rapidfuzz import process, fuzz
import pandas as pd


def column_search(df, col, score_cutoff=80):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data should be a Pandas DataFrame")
    if not isinstance(col, str):
        raise TypeError("column name should be provided as string")
    if not isinstance(score_cutoff, int):
        raise TypeError("score_cutoff should be an integer")

    column_to_match = col
    options = df.columns

    result = process.extract(query=column_to_match, choices=options,
                             limit=None, score_cutoff=score_cutoff)
    print(result)


def value_search(col, value):
    if not isinstance(col, pd.Series):
        raise TypeError("Input data should be a Pandas Series")
    if not isinstance(value, str):
        raise TypeError("value argument should be of type str")
    
    col = col.astype(str)
    result = process.extractOne(value, col, scorer=fuzz.ratio)
    print(result)

