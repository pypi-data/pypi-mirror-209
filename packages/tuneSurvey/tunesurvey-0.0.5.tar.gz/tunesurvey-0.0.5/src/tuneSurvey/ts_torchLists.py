"""Pytorch Models for sequentail data (non-iid rows or time/step dependence
        NNs for multi-row inputs and multiple(one row) output
        Train-one fit all with new samples using Dataloaders.
        Implement, LSTM and variations of transformers.
        See demo pt III
	Includes:
	
	create_sequences(data_seq_len) to build (without flattening n days, m vars) the X,y tensors. For 1 day per prediction, dimension of y is n*m
	create_n_seq_ts(data, seq_len, id_split) gives X,y,Xt,yt for train test split on i_split

	modelList_torch_ts - a modellist 
		this contains LSTM and Transformers (vanilla) so far which need the torch.nn, torch.optim. Note that nn.Transformer, nn.LSTM are called

	create_objective_ts(model_class, cv, tune_grid, opt_params, data, device, seq_len)
	  - returns an objective() for optuna.

	tscv = TimeSeriesSplit(n_splits=3)

objective = create_objective_ts(LSTM,tscv,lstm_grid,opt_grid,data,device, seq_len)

study = optuna.create_study(direction='minimize', pruner=optuna.pruners.MedianPruner())
study.optimize(objective, n_trials=100)	
	then, refer to the study object in Optuna.


	Speed: can be improved by using cuda or CPU parallel.
	With a short test cuda on 3090 is 3.5x the speed of i9 13900K on Z690
	Please follow the project for other benchmarks.
	...
	
	Troubleshooting of CUDA, pls use 
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"

	But note that most errors of values or memories are about the
dimension mismatch of the model class


        

"""
from copy import copy,deepcopy

modelList_torch_tsRegressor = []


def ts_aggregate_flatten(X, n_order, n_forward = 1, flatten_predictor = False, flatten_target = True):
    return null






import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

from sklearn.model_selection import TimeSeriesSplit



# Define LSTM model
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        output, _ = self.lstm(x)
        output = self.linear(output[:, -1, :])
        return output

# Define tuning grids
lstm_grid = {
    "num_layers": (1, 3),
    "hidden_size": (10, 100),
}


import torch
import optuna
import numpy as np
from sklearn.model_selection import TimeSeriesSplit















opt_grid = {"batch_size" : (8,16),
            "learning_rate": (1e-5, 1e-1),
            "num_epochs" : (100,150)}

modelList_torch_tsRegressor.append({"modelName":"LSTM_rollingTS",
                                    "modelInit": LSTM,
                                    "par": lstm_grid,
                                    "opt" : opt_grid,
                                    "from" : "torchTS"})




# Transformer for multivar time series, ordered n, predict 1 day per iteration


class TransformerModel(nn.Module):

    def __init__(self, input_size, output_size, n_heads, n_layers, dropout):
        super(TransformerModel, self).__init__()

        self.transformer_encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=input_size,
                nhead=n_heads,
                dropout=dropout
            ),
            num_layers=n_layers
        )
        self.decoder = nn.Linear(input_size, output_size)

    def forward(self, x):
        x = self.transformer_encoder(x)
        x = self.decoder(x[:, -1, :])
        return x

transformer_grid = {"n_heads" :[6,8,10],
                    "n_layers" : [2,4,6,8],
                    "dropout" : [.1,.2]}

modelList_torch_tsRegressor.append({"modelName":"Transformer_rollingTS",
                                    "modelInit": TransformerModel,
                                    "par": transformer_grid,
                                    "opt" : opt_grid,
                                    "from": "torchTS"})






