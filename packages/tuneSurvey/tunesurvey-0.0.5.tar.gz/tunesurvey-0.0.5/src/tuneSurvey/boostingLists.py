"""Boosting functions tuning - following sklearn models mostly

    XGBoost (version from DMLC) pip install xgboost
    lightGBM 
    CatBoost

"""

modelList_boosting = []

from xgboost import XGBRegressor, XGBClassifier



boostingc_grid = []
boostingr_grid = []

xgbc_grid = {"modelName":"XGBoostClassifier",
             "modelInit":XGBClassifier(),
            "par": {"n_estimators" : [10,100, 500, 1000],
                    "max_depth" : [3,5,7],
                    "eta" : [.01,.03,.1],
                    "colsample_by_tree" : [.7,.8,.9]},
            "from": "tabular",
            "inter" :True}
boostingc_grid.append(xgbc_grid)

xgbr_grid = {"modelName":"XGBoostRegressor",
             "modelInit":XGBRegressor(),
            "par": {"n_estimators" : [10,100, 500, 1000],
                    "max_depth" : [3,5,7],
                    "eta" : [.01,.03,.1],
                    "colsample_by_tree" : [.7,.8,.9]},
            "from": "tabular",
            "inter" :True}
boostingr_grid.append(xgbr_grid)



from catboost import CatBoostClassifier, CatBoostRegressor
catboostc_grid = {"modelName": "CatBoostClassifier",
                  "modelInit" : CatBoostClassifier(),
                  "par" : { 'iterations': 500,
                            'learning_rate': 0.1,
                            #'eval_metric': metrics.Accuracy(),
                            'random_seed': 42,
                            'logging_level': 'Silent',
                            'use_best_model': False
                        },
                  "from":"tabular",
                  "inter" :False}
boostingc_grid.append(catboostc_grid)
catboostr_grid = {"modelName":"CatBoostRegressor",
                  "modelInit" : CatBoostRegressor(),
                  "par" : { 'iterations': 500,
                            'learning_rate': 0.1,
                            #'eval_metric': metrics.Accuracy(),
                            'random_seed': 42,
                            'logging_level': 'Silent',
                            'use_best_model': False
                        },
                  "from":"tabular",
                  "inter":False}

boostingr_grid.append(catboostr_grid)
