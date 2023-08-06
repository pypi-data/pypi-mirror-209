import pandas as pd
import numpy as np
from pandas.api.types import is_object_dtype
from unidecode import unidecode


def find_nonascii(data, drop=False, remove=False, translate=False):

    if not (isinstance(data, pd.DataFrame) or isinstance(data, pd.Series)):
        raise TypeError("Input data must be a pandas DataFrame or Series")
    if isinstance(data, pd.Series) and not is_object_dtype(data):
        raise TypeError("Series must be of type object")
    if not isinstance(drop, bool):
        raise TypeError("'drop' parameter takes a boolean value")
    if not isinstance(remove, bool):
        raise TypeError("'remove' parameter takes a boolean value")
    if not isinstance(translate, bool):
        raise TypeError("'translate' parameter takes a boolean value")

    try:
        # For DataFrame
        df = data.select_dtypes(include=["object"]) 
    except AttributeError:
        df = data

    nonascii_dic = get_nonascii_dic(df)

    for key in nonascii_dic:
        # Solves issue of unequal value lengths in dic keys when converting dic to df
        nonascii_series = pd.DataFrame.from_dict({key: nonascii_dic[key]})

        if drop:
            try:
                # Works when data is series
                data = data[~data.apply(lambda x: x in nonascii_series.values)]
            except ValueError:
                mask = data.isin(nonascii_series).any(axis=1)
                data = data[~mask]
        elif remove:
            data = data.replace(nonascii_series.values, np.nan)
        elif translate:
            data = data.replace(nonascii_series.values, nonascii_series.applymap(unidecode).values)
            
    return data


def get_nonascii_dic(df):
    nonascii_dic = {}
    if isinstance(df, pd.DataFrame):
        for col in df.columns:
            nonascii_dic.update(get_nonascii_values(df[col]))
    else:
        nonascii_dic = get_nonascii_values(df)
    
    return nonascii_dic


def get_nonascii_values(series):
    nonascii_values = {}

    # Operations may fail with NAs
    notna = series[series.notna()]
    
    # .astype(str) catches error from non-string values
    nonascii = notna.astype(str).str.contains(r"[^\x00-\x7F]+", regex=True)

    if nonascii.any():
        nonascii_values[series.name] = series[nonascii.index].loc[nonascii[nonascii==True].index] 
    
    return nonascii_values













