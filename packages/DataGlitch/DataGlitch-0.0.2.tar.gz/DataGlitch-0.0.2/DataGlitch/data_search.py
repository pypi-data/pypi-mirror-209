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

    matches = process.extract(query=column_to_match, choices=options,
                             limit=None, score_cutoff=score_cutoff)
    
    for match in matches:
        print("Match: ", match[0])
        print("Similarity Score: ", match[1])
        print()


def value_search(col, value, score_cutoff=80):
    if not isinstance(col, pd.Series):
        raise TypeError("Input data should be a Pandas Series")
    if not isinstance(value, str):
        raise TypeError("value argument should be of type str")
    
    col = col.astype(str)
    matches = process.extract(value, col, scorer=fuzz.ratio, limit=None)
    
    # Filter matches above threshold
    filtered_matches = [match for match in matches if match[1] >= score_cutoff]
    for match in filtered_matches:
        print("Match: ", match[0])
        print("Similarity Score: ", match[1])
        print()

