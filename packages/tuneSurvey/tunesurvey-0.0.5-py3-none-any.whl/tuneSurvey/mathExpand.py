"""Enrich difference features
"""
import math
from copy import copy

from statsmodels.tsa.stattools import adfuller

def expand_diff(df,order = 2, drop_origional = False):
    """df is a DataFrame
"""
    var_num = df.select_dtypes(include=np.number).columns.tolist()
    for v in var_num:
        for k in range(order):
            lag=np.array(df[v])

            lag=np.concatenate((np.repeat(0,k),lag[0:(n-k)]))
            df[v+"lag"+str(k+1)] = lag
    df2=df
    if drop_origional:
        df2 = df2.drop(var_num)
    return df2

def expand_unary_num(df,fn,rename = lambda v: "feature_"+v, drop_origional = False):
    var_num = df.select_dtypes(include=np.number).columns.tolist()
    for v in var_num:
        rename_v = list(map(fn, np.array(df_v)))
        df[rename(v)] = rename_v

    df2=df
    if drop_origional:
        df2 = df2.drop(var_num)
    return df2

def difference_until_stationery(df,n_max, conf_level = .05,
                                criteria = lambda ps: all(ele < conf_level for ele in ps)):
    """Differencing the dataframe until every column(as time series) passes ADFuller test.
"""
    p_by_order = []
    for i in range(n_max):
        df2 = expand_diff(copy(df),order=i+1, drop_origional= True)[0:]
        n_df = np.array(df2)
        nr =n_df.shape[1]
        ps = []
        for j in range(nr):
            #print(ti)
            ps.append(adfuller(n_df[:,j])[1])
        p_by_order.append(ps)
        if criteria(ps):
            return df2, p_by_order
    return df2, p_by_order

def difference_with_log_until_stationery(df,n_max, conf_level = .05,
                                criteria = lambda ps: all(ele < conf_level for ele in ps)):
    """Differencing the dataframe until every column(as time series) passes ADFuller test.
"""
    p_by_order = []
    p_by_order_log = []
    for i in range(n_max):
        df2 = expand_diff(copy(df),order=i+1, drop_origional= True)[0:]
        n_df = np.array(df2)
        nr =n_df.shape[1]
        ps = []
        for j in range(nr):
            #print(ti)
            ps.append(adfuller(n_df[:,j])[1])
        p_by_order.append(ps)
        if criteria(ps):
            return df2, p_by_order
        df2 = expand_unary_num(df2,math.log, lambda v: "log"+v, drop_origional = True)

        ps2 = []
        for j in range(nr):
            #print(ti)
            ps2.append(adfuller(n_df[:,j])[1])
        p_by_order_log.append(ps2)
        if criteria(ps2):
            return df2, p_by_order_log
        
    return df2, p_by_order, p_by_order_log

        
        

