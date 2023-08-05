"""forceCollect: given a model dict, data, cv and score(s) options
force collect the time and score vectors to file(s) without reduction.
the function uses expanded form of parameters and assigns a folder for  saving.
e

Reminder:

pd.DataFrame(ds)  transfers a list of Dicts (must have same keys) to a DataFrame
df.to_dict('records') is the inverse

"""

from sklearn.model_selection import ParameterGrid
import pandas as pd
from copy import copy,deepcopy
from time import time
import pickle
import os

param_grid = {'a': [1, 2], 'b': [True, False]}
pgd = ParameterGrid(param_grid)

pgdf = pd.DataFrame(pgd)

def forceCollect_sk(m, pgd, data, cv, scorers, path="forceCollect"):
    """Brute force collection of all models
    for sklearn cv objects
    for SKLEARN models
    for STATIC TABULAR DATA ONLY
    m - dict that contains
     |_ modelInit -  model instance
     |_ par - hyperparams
     |_ from : whether this model is from
         sk/skTS/torchTS. this deal with sk only
    pgd - the EXPANDED parameter grid in a list of dicts.
    cv object MUST HAVE ids exported in the iterations, e.x. sklearn.TimeSeriesSplit()
    scorers,  a Dict of function {<ScorerName>: scorer} for scoring/ recording
    path - relative path to save the models

    the output of the model is a list of performance on the n th cvs and time.

    """
    os.mkdir(path)

    pgdf = pd.dataframe(pgd)
    assert m["from"] == "sk"
    gd_result = []


    try:
        modelname =  m["name"]
    except:
        modelname = type(str(m["modelInit"]().__name__))
    id_par = 0
    for par in pgd:
        #fold_results = []
        id_fold = 0
        for train_idx, val_idx in cv.split(data):
            train_X_fold, train_y_fold = train_X[train_idx], train_y[train_idx]
            val_X_fold, val_y_fold = train_X[val_idx], train_y[val_idx]

            t0 = time()
            modelInit = deepcopy(m["modelInit"])

            model = modelInit(**par).fit(train_X_fold, train_y_fold)

            filename = path + "/" + modelname + str(id_par)+ "_"+ str(id_fold)
            
            pickle.dump(model, open(filename, "wb"))


            y_pred = model.predict(val_y_fold)
            id_fold+=1

            scores = [id_par,id_fold]
            scores.append(time() - t0)
            score_names = ["id_par","id_fold","time"]
            for k, v in scorers:
                scores.append(v(val_y_fold, y_pred))
                score_names.append(k)

            gd_results.append(scores)
            #fold_results.append(scores)
        id_par+=1
    return pd.DataFrame(gd_results, columns = score_names)
                
                    

    
