import pandas as pd
import numpy as np
from itertools import combinations, permutations

def pairwise(df, operation, columns = None):
    """Form interactions between all pairs of numeric columns

    Arguments:
        df -- the DataFrame to run on
        operation -- the operation(s) to compute between pairs
        columns -- specify a subset of columns to consider

    Possible operations are:
        'sum', 'difference', 'product', 'ratio',
        'power', 'root', 'log', 'arctan', 'mod',
        'arctanh', 'l1', 'l2', 'max' or 'all'
    """
    result = pd.DataFrame(index=df.index)
    if columns is None:
        columns = [c for c in df.columns if np.issubdtype(df[c], np.number)]


    if operation == 'all':
        operation = ['sum', 'difference', 'product', 'ratio',
                     'power', 'root', 'log', 'arctan', 'mod',
                     'arctanh', 'l1', 'l2', 'max']

    if type(operation) is list:
        if 'all' in operation:
            raise ValueError("No point in a list containing 'all', silly.")
        operation = pd.unique(operation)
        return pd.concat(
            [pairwise(df, op, columns) for op in operation],
            axis=1
        )

    if operation == 'sum':
        f = lambda df, c1, c2: df[c1]+df[c2]
        pairs = combinations(columns, 2)
        name = '%s + %s'
    elif operation == 'difference':
        f = lambda df, c1, c2: df[c1]-df[c2]
        pairs = combinations(columns, 2)
        name = '%s - %s'
    elif operation == 'product':
        f = lambda df, c1, c2: df[c1]*df[c2]
        pairs = combinations(columns, 2)
        name = '%s * %s'
    elif operation == 'ratio':
        f = lambda df, c1, c2: df[c1]/df[c2]
        pairs = permutations(columns, 2)
        name = '%s / %s'
    elif operation == 'power':
        f = lambda df, c1, c2: df.loc[df[c2]>=0,c1]**df.loc[df[c2]>=0,c2]
        pairs = permutations(columns, 2)
        name = '%s ^ %s'
    elif operation == 'root':
        f = lambda df, c1, c2: df[c1]**(1/df[c2])
        pairs = permutations(columns, 2)
        name = "%s to %s'th root"
    elif operation == 'log':
        f = lambda df, c1, c2: np.log(df[c2])/np.log(df[c1])
        pairs = permutations(columns, 2)
        name = 'log_%s %s'
    elif operation == 'arctan':
        f = lambda df, c1, c2: np.arctan(df[c1]/df[c2])
        pairs = combinations(columns, 2)
        name = 'arctan(%s / %s)'
    elif operation == 'mod':
        f = lambda df, c1, c2: df[c1] % df[c2]
        pairs = permutations(columns, 2)
        name = '%s mod %s'
    elif operation == 'arctanh':
        f = lambda df, c1, c2: np.arctanh((df[c1]/df[c2]).clip(-1,1))
        pairs = permutations(columns, 2)
        name = 'arctanh(%s/%s)'
    elif operation == 'l1':
        f = lambda df, c1, c2: df[c1].abs() + df[c2].abs()
        pairs = combinations(columns, 2)
        name = '||%s - %s||_2'
    elif operation == 'l2':
        f = lambda df, c1, c2: (df[c1]**2+df[c2]**2)**0.5
        pairs = combinations(columns, 2)
        name = '||%s - %s||_2'
    elif operation == 'max':
        f = lambda df, c1, c2: df[[c1, c2]].abs().max(axis=1)
        pairs = combinations(columns, 2)
        name = 'max(%s, %s)'
    else:
        raise ValueError(
            "'%s' is not a supported interaction." % operation
        )

    for c1, c2 in pairs:
        result[name % (c1,c2)] = f(df, c1, c2)
    
    return result