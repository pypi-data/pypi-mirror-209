"""Subsetting a big dataframe to smaller ones to rerun models"""

def subsetting_timestep(df, timeStep, i_include):
    """df - dataframe
    timeStep: timeStep gap for each step
    ic number of columns to include
    """
    l = len(df)
    i=0
    dfs = []
    while i + i_include < l :
        dfs.append(df.iloc[i:(i+i_include),:])
    return dfs

