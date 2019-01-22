# featurama
A collection of utilities for quickly creating many features for use in ML models.

## interactions
Module for computing interaction features in datasets

### pairwise
`pairwise(df, operation, columns = None)`
Form interactions between all pairs of numeric columns

Arguments:
    df -- the DataFrame to run on
    operation -- the operation(s) to compute between pairs
    columns -- specify a subset of columns to consider

Possible operations are:
    ```
    'sum', 'difference', 'product', 'ratio',
    'power', 'root', 'log', 'arctan', 'mod',
    'arctanh', 'l1', 'l2', 'max', 'all'
    ```
