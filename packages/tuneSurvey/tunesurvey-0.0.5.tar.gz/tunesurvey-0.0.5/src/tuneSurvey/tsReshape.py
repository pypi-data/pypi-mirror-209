

def time_category_aggregate(df, timeIdentifier, spaceGroupIdentifier, timeStep=1, i_include=1, need_sort = True):
    """turn dataframe with time, space-group observation rows into rows with unique time id
    (sequential), count by each space-group with an interval containing i_include terms, with increment timeStep.
    complexity is close to sorting.(need_sort=True).
    If pre-sorted w.r.t. time is done, then need only approx O(n) time for n=number of rows in the origional df.
    """

    max_time_diff = max(df[timeIdentifier])


    #df = df.dropna(how='any')
    df = df.sort_values([timeIdentifier])
    spaceVec = list(set(list(df[spaceGroupIdentifier])))

    c_along_spaceVec = range(len(spaceVec)) # unique location identifier
    space_map_c = list(map(lambda x: spaceVec.index(x),df[spaceGroupIdentifier])) #this can be even faster by int(PDQ)
    timeVec = list(set(list(df[timeIdentifier])))
    l = len(df)
    ts_aggregate = []
    t1=time()

    i=0

    while i+i_include<l:
        space_aggregate = np.zeros(len(spaceVec),int)
        for j in range(i,i+i_include):
            space_aggregate[space_map_c[j]]+=1 #can also be faster eliminating i_include>timestep
        ts_aggregate.append(space_aggregate)
        i+=timeStep

    return pd.DataFrame(ts_aggregate,columns = spaceVec)



