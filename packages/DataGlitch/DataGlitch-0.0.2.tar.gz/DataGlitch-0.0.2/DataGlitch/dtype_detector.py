import pandas as pd
from pandas.api.types import is_object_dtype
import re

def find_numeric(data):
    if not isinstance(data, pd.Series):
        raise TypeError(f"Input data must be a pandas Series not {type(data)}")
    if not is_object_dtype(data):
        raise TypeError(f"Series {data.name} must be of the object data type")
    
    unique_values = tuple(data.dropna().unique())
    numeric_values, ambiguous_values = exhaustive_search(unique_values)

    print(f"numeric: {len(data[data.isin(numeric_values)])}\nambiguous: {len(data[data.isin(ambiguous_values)])}\nother: {len(data[~data.isin(numeric_values) & ~data.isin(ambiguous_values)])}")
        
    # Return subsets for numeric, ambiguous and string values
    return data[data.isin(numeric_values)], data[data.isin(ambiguous_values)], data[~data.isin(numeric_values) & ~data.isin(ambiguous_values)]
    

def exhaustive_search(unique_values):
    # Numeric values 
    regx = re.compile(r"^[-+]?(?:(?:\d+ |\d*[,\.])?\d+(?:[Ee][-+]?(?:\d+|\d+\/\d+|\d*[,\.]\d+)|[,\.]\d+(?:[,\.]\d+)?)?|\d+\/\d+)$") # previous regx = r"^(?:[-+]?)(?:\d+|\d*[,\.]\d+)(?:[Ee][-+]?\d+)?|\d+/[1-9]\d*$"
    # non-numeric at front (e.g. '$50')
    regx_front = re.compile(regx.pattern[0] + "\D+" + regx.pattern[1:])
    # non-numeric at end (e.g. '50p')
    regx_end = re.compile(regx.pattern[:-1] + "\D+" + regx.pattern[-1])

    numeric_values = tuple(val for val in unique_values if (isinstance(val, str) and regx.search(val)) or ((isinstance(val, int) or isinstance(val, float)) and not isinstance(val, bool))) 
    ambiguous_values = tuple(val for val in unique_values if val not in numeric_values and isinstance(val, str) and (regx_front.search(val) or regx_end.search(val)))

    return numeric_values, ambiguous_values