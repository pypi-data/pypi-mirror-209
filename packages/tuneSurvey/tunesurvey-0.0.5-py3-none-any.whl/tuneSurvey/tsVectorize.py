"""Vectorize models with given 1 term prediction
    
"""
import pickle
import numpy as np
from copy import copy,deepcopy

from sklearn.model_selection import GridSearchCV


def split_tscv_by_order_features(rawdata, order_features):
    """
    to protect origional vector, do from copy import deepcopy"""
    n_obs, n_var = rawdata.shape
    X = np.zeros([n_obs-order_features, order_features*n_var])
    #yjs are the columns
    for i in range(n_obs - order_features):
        for j in range(order_features):
            for k in range(n_var):
                X[i,k+j*n_var] = rawdata[i+j,k]

    X_usable = X
    Y_usable = rawdata[order_features:,:]#
    return X_usable, Y_usable
    




def vectorized_Search_hyperparameter(model, parameters, X, Y,cv =  5,search_function = GridSearchCV,verbose =False, path = "vec_search", modelName = "Unnamed"):
    """
    # model - type of model (SVR(), randomForest()...)
    # X - predictor - all rows of X are used for prediction, but each model only gives on entry in Y
    # Y - matrix containing n_var number of column vectors as target of the prediction
    # cv - cross validation type (scikit-learn obj) passed in to model selection type.
    # cv is either a number for k fold or a model selection obj for esample, cv = TimeSeriesSplit(n_splits=2, max_train_size=None, test_size=2, gap=0)
    """
    
    
    #Series with verbose for debugging
    n_obs, n_var = Y.shape
    m_Yi = []# Collecting the model for each term in the row of the time series
    for i in range(n_var):
        try:
            if verbose:
                print("working on:" + str(modelName),"model",i)
            m_Yij = search_function(model, param_grid = parameters, cv=cv).fit(X,Y[:,i])

            if save_searches:


                filename = path + "/" + modelname + str(i)
                
                pickle.dump(m_Yij, open(filename, "wb"))


            m_Yi.append(m_Yij)
        except:
            print("Err during " + str(i))
    return m_Yi

from joblib import parallel_backend

def vectorized_Search_hyperparameter_modelDict(modelDict, X, Y,cv =  5,search_function = GridSearchCV,verbose =False, path = "vec_search",save_searches=True, inter=True):
    """
    # model - type of model (SVR(), randomForest()...)
    # X - predictor - all rows of X are used for prediction, but each model only gives on entry in Y
    # Y - matrix containing n_var number of column vectors as target of the prediction
    # cv - cross validation type (scikit-learn obj) passed in to model selection type.
    # cv is either a number for k fold or a model selection obj for esample, cv = TimeSeriesSplit(n_splits=2, max_train_size=None, test_size=2, gap=0)
    """

    model = modelDict["modelInit"]
    try:
        modelName = modelDict["modelName"]
    except:
        modelName = model.__class__.__name__
    parameters = modelDict["par"]
    model = modelDict["modelInit"]
    #Series with verbose for debugging
    n_obs, n_var = Y.shape
    m_Yi = []# Collecting the model for each term in the row of the time series
    for i in range(n_var):
        try:
            if verbose:
                print("working on:" + str(modelName),"model",i)
            if inter and modelDict["inter"]==True:
                with parallel_backend('threading', n_jobs=-1):
                    m_Yij = search_function(model, param_grid = parameters,cv=cv).fit(X,Y[:,i])
            else:
                m_Yij = search_function(model, param_grid = parameters,cv=cv).fit(X,Y[:,i])


            if save_searches:


                filename = path + "/" + modelName + str(i)
                
                pickle.dump(m_Yij, open(filename, "wb"))


            m_Yi.append(m_Yij)
        except:
            print("Err during " + str(i))
    return m_Yi

def vectorized_Search_hyperparameter_multimodelDict(modelList,X,Y,cv=5,search_function=GridSearchCV,verbose=False,path = "vec_search"):
    # modelList contains subLists of models, and parameters and maybe types (regressor) or criterion in the future
    
    # model |best par|best fit result|... path to save the model?
    resultList = []
    n_obs, n_var = Y.shape
    for i,m in enumerate(modelList):
        modelClassName = m["modelInit"].__class__.__name__
        if verbose:
            print("working on:"+str(modelClassName))
        m_Yi = vectorized_Search_hyperparameter_modelDict(m, X, Y,cv,search_function,verbose, path)
        
        resultList.append(m_Yi.deepcopy())
    return resultList
    




def vectorized_Search_hyperparameter_multimodel(modelList,X,Y,cv=5,search_function=GridSearchCV,verbose=False):
    # modelList contains subLists of models, and parameters and maybe types (regressor) or criterion in the future
    
    # model |best par|best fit result|... path to save the model?
    resultList = []
    n_obs, n_var = Y.shape
    for i,m in enumerate(modelList):
        modelClassName = m["modelInit"].__class__.__name__
        if verbose:
            print("working on:"+str(modelClassName))
        m_Yi = []# Collecting the model for each term in the row of the time series
        for j in range(n_var):
            if verbose:
                print("working on:model",j)
            m_Yi.append(search_function(m["modelInit"], param_grid = m["par"], cv=cv).fit(X,Y[:,j]))
        resultList.append(m_Yi.copy())
    return resultList


def saveModelList_s(modelList,X,Y,path="sklModels",verbose=False):
    """save a list of model named by modelSequence() convention"""
    pgd = ParameterGrid(modelList['par'])
    if verbose:
        print("Permutating models and saving")
    for i, pars in enumerate(pgd):
        m = deepcopy(modelList['modelInit'])
        if verbose:
            print(pars)
            print(m)
        m = m(**pars)
        m.fit(X,Y)
        filename = ""
        for k,val in pars.items():
            filename += k+str(val).replace(".","-")
            
        dump(m,os.path.join(path,filename+".joblib"))
        gc.collect()


def modelSequence(par):
    """get names of saved files in a modelList"""
    pgd = ParameterGrid(par)
    s = []
    

    
    for i, pars in enumerate(pgd):
        
        filename = ""
        for k,val in pars.items():
            filename += k+str(val).replace(".","-")
        s.append(filename)
    return s


# X exterior train
# Y exterior test

def vectorize_model(X,Y,mtd):
    """
    #m - fitted model
    #mtd - method to create the model, e.x. SVM(parameters....).fit(data...)
    """
    n_var = Y.shape[2]
    modelList = []
    for i in range(n_var):
        m = mtd(X,Y[i])
        modelList.append(X,Y[i],m)
    return modelList

def rolling_1_day_vectorize_model(X,Y,predmtd):
    
    Y_t = np.empty_like(Y)
    
    nr, nc = Y.shape
    for i in range(nr):
        for j in range(nc):
            mj = deepcopy(predmtd[j])
            Y_t[i,j] = mj(X)
        X = Y_t[i,:]
    return Y_t
    
def sample_1_day_vectorize_model(X,Y,predmtd):
    Y_t = np.empty_like(Y)
    
    nr, nc = Y.shape
    for i in range(nr):
        for j in range(nc):
            mj = deepcopy(predmtd[j])
            Y_t[i,j] = mj(X)
        X = Y[i,:]
    return Y_t

def ts_feature_flatten(df,n):
    """flatten time series df (each row is one time unit), flatten all features prev n days to a row"""
    order_features = n
    n_obs,n_var = df.shape
    X = np.zeros([n_obs-order_features+1, order_features*n_var])
    #yjs are the columns
    for i in range(n_obs - order_features+1):
        for j in range(order_features):
            for k in range(n_var):
                X[i,k+j*n_var] = df[i+j,k]
    return X




def append_rolling_vectorize_model(train,test,predmtd,n=1,verbose =False):
    """ one fit rolling prediction
    predmtd is a list of function each taking in all features to predict one term in y.
    n - order that prediction model requires
     train ORIGIONAL ts df
    """
    Y_t = np.empty_like(test)
    
    nr, nc = Y_t.shape
    
    rolling_df  = train[-n:,:]
    X = ts_feature_flatten(rolling_df,n=n)
    if verbose:
        print(X)
    
    for i in range(nr):
        for j in range(nc):
            mj = predmtd[j]
            Y_t[i,j] = mj(X)
        rolling_df = np.concatenate((rolling_df[-n+1:,:],Y_t[[i],:]))
        if verbose:
            print(rolling_df)
        X = ts_feature_flatten(rolling_df,n=n)
    return Y_t

def append_rolling_vectorize_model_with_sample(train,test,predmtd,n=1):
    """ one fit rolling prediction
    n - order that prediction model requires
    train ORIGIONAL ts df
    """
    Y_t = np.empty_like(test)
    
    nr, nc = Y_t.shape
    
    rolling_df  = train[-n:,:]
    X = ts_feature_flatten(rolling_df,n=n)
    
    
    for i in range(nr):
        for j in range(nc):
            
            mj =predmtd[j]
            Y_t[i,j] = mj(X)
        rolling_df = np.concatenate((rolling_df[-n+1:,:],test[[i],:]))
        X = ts_feature_flatten(rolling_df,n=n)
    return Y_t


def reduce_best_rolling_predictor_s(predictorList, Y_train, Y_test, criterion,n, verbose = False):
    """find which row is the best predictor"""
    nModels = len(predictorList)
    nVars = len(predictorList[0])
    current_best_score = float('-inf')
    for i in range(nModels):
        predictorVec = predictorList[i]
        score_1 = criterion(Y_train,Y_test, predictorVec,n)
        if score_1>current_best_score:
            
            current_best_score = score_1
            best_model_index = deepcopy(i)
            if verbose:
                print("current best model index  ", best_model_index, "score ", score_1)
    return best_model_index


def reduce_best_rolling_predictor(predictorList, Y_train, Y_test, criterion,n, verbose = False):
    """Find which combination (one model for each term) gives the best model, combine into a row of predictors
    used in append_rolling_vectorized_modell_with_sample()"""
    nModels = len(predictorList)
    nVars = len(predictorList[0])
    current_best_score = float('-inf')
    for i in itertools.product(*list(itertools.repeat(list(range(nModels)),nVars))):
        predictorVec = []
        col=0
        
        for j in i:
            predictorVec.append(predictorList[j][col])
            col += 1
        score_1 = criterion(Y_train,Y_test, predictorVec,n)
        if score_1>current_best_score:
            current_best_score = score_1
            best_model_index = deepcopy(i)
            if verbose:
                print("current best model index  ", best_model_index)
    return best_model_index













import optuna

from sklearn.metrics import mean_squared_error
from torch.utils.data import DataLoader, TensorDataset

import torch

def create_sequences(data, seq_len):
    X = []
    y = []
    for i in range(seq_len, len(data)):
        X.append(torch.tensor(data[i-seq_len:i,:]))
        y.append(torch.tensor(data[i, :]))
        
    X_tensor = torch.stack(X)
    y_tensor = torch.stack(y)
    return X_tensor, y_tensor

def create_n_seq_ts(data,seq_len,id_split):
    """
    #seq_len=5
    #x,y,xt,yt = create_n_seq_ts(data,seq_len,90)
    """
    X,y = create_sequences(data=data,seq_len=seq_len)
    
    return X[0:id_split,:], y[0:id_split,:], X[id_split:,:], y[id_split:,:]



def create_objective_ts(model_class, cv, tune_grid, opt_params,data, device, seq_len,modelName = "Unnamed",path = "tsNN_search"):
    """
    Returns an objective() function to be optimized by Optuna

    tscv = TimeSeriesSplit(n_splits=3)

    objective = create_objective_ts(LSTM,tscv,lstm_grid,opt_grid,data,device, seq_len)

    study = optuna.create_study(direction='minimize', pruner=optuna.pruners.MedianPruner())
    study.optimize(objective, n_trials=100)

    # Print best hyperparameters and loss
    print('Best hyperparameters:', study.best_params)
    print('Best loss:', study.best_value)


"""
    nVar = data.shape[1]
    def objective(trial):
        # Sample hyperparameters from tuning grid
        params = {param_name: trial.suggest_categorical(param_name, param_values) 
                  for param_name, param_values in tune_grid.items()}
        params['input_size'] = nVar
        params['output_size'] = nVar
        # Initialize model
        model = model_class(**params)
        model.to(device)
        
        # Define loss function and optimizer
        criterion = torch.nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=trial.suggest_categorical('learning_rate',opt_params['learning_rate']))
        
        num_epochs = trial.suggest_categorical('num_epochs',opt_params['num_epochs'])
        batch_size = trial.suggest_categorical('batch_size',opt_params['batch_size'])
        
        # Train and evaluate model using cross-validation
        val_losses = []
        for train_idx, val_idx in cv.split(data):

            id_split = val_idx[0]
            
            train_X_fold, train_y_fold, val_X_fold, val_y_fold = create_n_seq_ts(data[:val_idx[-1]+1,:],seq_len,id_split)
            train_X_fold = train_X_fold[train_idx[0]:]
            train_y_fold = train_y_fold[train_idx[0]:]
            train_dataset = TensorDataset(train_X_fold.float(), 
                                          train_y_fold.float())#.to(device)
            train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

            val_dataset = TensorDataset(val_X_fold.float(), 
                                        val_y_fold.float())#.to(device)
            val_loader = DataLoader(val_dataset, batch_size=1, shuffle=False)# only load 1 entry of data to predict next 1 day
            
            
            for epoch in range(num_epochs):
                model.train()
                for inputs, targets in train_loader:
                    inputs = inputs.to(device)
                    targets = targets.to(device)
                    
                    optimizer.zero_grad()
                    
                    outputs = model(inputs)
                    
                    loss = criterion(outputs, targets)
                    loss.backward()
                    optimizer.step()

                model.eval()
                with torch.no_grad():
                    val_loss = 0
                    for inputs, targets in val_loader:
                        inputs = inputs.to(device)
                        targets = targets.to(device)

                        outputs = model(inputs)
                        val_loss += criterion(outputs, targets).item()
                    val_loss /= len(val_loader)
                    val_losses.append(val_loss)

                trial.report(val_loss, epoch)

                if trial.should_prune():
                    raise optuna.exceptions.TrialPruned()
            filename = path + "/" + modelName+ str(trial.number)
            
            try:
                #path = "tsNN_search"
                
                pickle.dump(model, open(filename, "wb"))
                
                
            except:
                print("saving" +filename+"failed in TS torch")
        loss_score = float(np.mean(val_losses))
        return loss_score
    return objective




def create_objective_ts_modelDict(modelDict, cv, data, device, seq_len, path = "tsNN_search"):
    """
    Returns an objective() function to be optimized by Optuna

    tscv = TimeSeriesSplit(n_splits=3)

    objective = create_objective_ts(LSTM,tscv,lstm_grid,opt_grid,data,device, seq_len)

    study = optuna.create_study(direction='minimize', pruner=optuna.pruners.MedianPruner())
    study.optimize(objective, n_trials=100)

    # Print best hyperparameters and loss
    print('Best hyperparameters:', study.best_params)
    print('Best loss:', study.best_value)


"""
    modelName = modelDict["modelName"]
    tune_grid = modelDict["par"]
    opt_params = modelDict["opt"]
    model_class = modelDict["modelInit"]
    nVar = data.shape[1]
    def objective(trial):
        # Sample hyperparameters from tuning grid
        params = {param_name: trial.suggest_categorical(param_name, param_values) 
                  for param_name, param_values in tune_grid.items()}
        params['input_size'] = nVar
        params['output_size'] = nVar
        # Initialize model
        model = model_class(**params)
        model.to(device)
        
        # Define loss function and optimizer
        criterion = torch.nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=trial.suggest_categorical('learning_rate',opt_params['learning_rate']))
        
        num_epochs = trial.suggest_categorical('num_epochs',opt_params['num_epochs'])
        batch_size = trial.suggest_categorical('batch_size',opt_params['batch_size'])
        
        # Train and evaluate model using cross-validation
        val_losses = []
        for train_idx, val_idx in cv.split(data):

            id_split = val_idx[0]
            
            train_X_fold, train_y_fold, val_X_fold, val_y_fold = create_n_seq_ts(data[:val_idx[-1]+1,:],seq_len,id_split)
            train_X_fold = train_X_fold[train_idx[0]:]
            train_y_fold = train_y_fold[train_idx[0]:]
            train_dataset = TensorDataset(train_X_fold.float(), 
                                          train_y_fold.float())#.to(device)
            train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

            val_dataset = TensorDataset(val_X_fold.float(), 
                                        val_y_fold.float())#.to(device)
            val_loader = DataLoader(val_dataset, batch_size=1, shuffle=False)# only load 1 entry of data to predict next 1 day
            
            
            for epoch in range(num_epochs):
                # Train model
                model.train()
                for inputs, targets in train_loader:
                    inputs = inputs.to(device)
                    targets = targets.to(device)
                    
                    optimizer.zero_grad()
                    
                    outputs = model(inputs)
                    
                    loss = criterion(outputs, targets)
                    loss.backward()
                    optimizer.step()

                # Evaluate model on validation set
                model.eval()
                with torch.no_grad():
                    val_loss = 0
                    for inputs, targets in val_loader:
                        inputs = inputs.to(device)
                        targets = targets.to(device)

                        outputs = model(inputs)
                        val_loss += criterion(outputs, targets).item()
                    val_loss /= len(val_loader)
                    val_losses.append(val_loss)

                trial.report(val_loss, epoch)
                # Prune if necessary
                save = True
                if trial.should_prune():
                    save = False
                    raise optuna.exceptions.TrialPruned()
        filename = path + "/" + modelName+ str(trial.number)
        
        try:
            #path = "tsNN_search"

            if save:
                pickle.dump(model, open(filename, "wb"))
            
            
        except:
            print("saving" +filename+"failed in TS torch")
        loss_score = float(np.mean(val_losses))
        return loss_score
    return objective






def vsearch_modelList(modelList, data, seq_len, cv, device):
    
    r = []
    for modelDict in modelList:
        try:            
            if modelDict["from"] ==  "tabular":
                X, Y = split_tscv_by_order_features(data,seq_len)
                ri = vectorized_Search_hyperparameter_modelDict(modelDict, X, Y,cv ,search_function = GridSearchCV,verbose =False, path = "vec_search")
                

                
            elif modelDict["from"] == "torchTS":
            
                
                objective = create_objective_ts_modelDict(modelDict, cv, data, device, seq_len)
                study = optuna.create_study(direction='minimize', pruner=optuna.pruners.MedianPruner())
                study.optimize(objective, n_trials=100)
                ri = study
        except:
            X, Y = split_tscv_by_order_features(data,seq_len)
            ri = vectorized_Search_hyperparameter_modelDict(modelDict, X, Y,cv ,search_function = GridSearchCV,verbose =False, path = "vec_search")
        r.append(deepcopy(ri))

        
    return r



