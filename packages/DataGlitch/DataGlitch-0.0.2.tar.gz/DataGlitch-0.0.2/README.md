# DataGlitch: _A Python Toolkit for Messy Data_

DataGlitch is a Python package designed to address common data challenges in a pandas DataFrame, including handling mixed data types, non-ASCII values, and facilitating dataset exploration. 

```
pip install DataGlitch
```

<br>

## Usage
DataGlitch currently offers three functionalities:
- `dtype_detector`: Find mixed data types in columns. 
- `nonascii_handler`: Detect and handle non-ASCII characters.
- `data_search`: Search for the existence of specific columns or values.

<br>
<hr>
<br>

### dtype_detector

The `dtype_detector` uses regular expressions to detect different data types in a column through the `find_numeric()` function. This function takes a pandas Series with data type `Object` as an argument and returns three new variables: `numeric`, `ambiguous` and `non_numeric`. Each of these contain a subset of the original column.

`numeric` can contain any numeric value or any string value interpreted as numeric by the regular expression:
-	Integers: whole numbers, both positive and negative. Examples: `-42`, `123`. 
-	Floating-point numbers: decimal numbers, both positive and negative. Examples: `-3.14`, `0.5`. 
-	Numbers in scientific notation. Examples: `1.23e-4`, `-2E+10`. 
-	Fractions: fractions in the form of numerator/denominator. Examples: `1/2`, `-3/4`. 
-	Numbers with comma or dot as decimal separator. Examples: `1,000`, `3.5`. 
-	Numbers with multiple decimal separators (comma or dot). Examples: `1.0.0`, `2,000.5.6`.

`ambiguous` can contain any value that is interpreted as numeric by the regular expression if it also has alphabetic or special characters at its front or end. Examples: `50cents`, `$10`.

`non_numeric` can contain any value that is not classified as `numeric` or `ambiguous`. Examples: `2000-01-01`, `DataGlitch6000!`.

<br>

```
# Import and apply
from DataGlitch.dtype_detector import find_numeric
numeric, ambiguous, non_numeric = find_numeric(df["col"])
```
Example operations:

```
# Drop non_numeric subset from dataframe
df = df[~df["col"].isin(non_numeric)]
```

```
# Replace values in subset with NAs
import numpy as np
df.loc[df["col"].isin(non_numeric), "col"] = np.nan
```

Other operations can occur directly on the dataframe. For instance, if wanting to correct comma-separated floats that have been identified in the column:
```
df["col"] = df["col"].replace(",", ".", regex=True)
```

<br>
<hr>
<br>

### nonascii_handler

The `nonascii_handler` uses the `find_nonascii()` function to locate rows/values with non-ascii characters in a DataFrame or Series with data type `Object`. For handling non-ascii, the user is offerred three options:
1. Drop all rows that contain non-ascii values by setting the `drop` parameter to `True`.
2. Replace values with non-ascii with `np.nan` to indicate missigness by setting the `remove` parameter to `True`.
3. Translate values with non-ascii with the `unidecode` library by setting the `translate` parameter to `True`.

If none of the above options are selected, the data is returned as is (default).

```
from DataGlitch.nonascii_handler import find_nonascii
df_ascii = find_nonascii(df, drop=False, remove=False, translate=True)
```

<br>
<hr>
<br>

### data_search

`data_search` performs fuzzy string matching through the `rapidfuzz` library. It looks for the existance of columns in a dataset or particular values within a column. 

```
from data_search import column_search, value_search
```

Columns are identified through the `column_search()` function which takes a pandas DataFrame, the name of the column as a string, and a cut-off score which defaults to 80. The output contains any matches and their similarity score. For a less strict search, the cut-off score can be lowered.

```
column_search(df, "column_name", score_cutoff=80)
```

The `value_search()` function looks for the existance of a value in a pandas Series. Even if the value under investigation is integer/float, it should still be passed as string to the function. The output includes  any matches and their similarity score.

```
value_search(df["col"], "value", score_cutoff=80)
```




