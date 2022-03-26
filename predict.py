import pandas as pd
import lightgbm as lbm
from sklearn.model_selection import RepeatedKFold,train_test_split,cross_val_score
import os
import glob

def predict(X):
    scores = pd.read_csv(os.path.join('data','scores.csv'))
    conditions = glob.glob(os.path.join('data','condition','')+'*')
    control = glob.glob(os.path.join('data','control','')+'*')

    conditions_list = []
    control_list = []
    for file in conditions:
        d = pd.read_csv(file).describe().T
        d['number']=os.path.basename(file)[:-4]
        conditions_list.append(d)
    for file in control:
        d = pd.read_csv(file).describe().T
        d['number']=os.path.basename(file)[:-4]
        control_list.append(d)

    control_df = pd.concat(control_list)
    conditions_df = pd.concat(conditions_list)

    final_data = pd.concat([conditions_df,control_df])
    df = scores.merge(final_data,on='number')
    df = df.fillna(0)

    df = df.drop(['edu','age'],axis=1)

    X = df.drop(['afftype','number'],axis=1)
    y = df['afftype']
    X_train, X_test, y_train, y_test = train_test_split(X, y)


    model = lbm.LGBMClassifier()
    model.fit(X_train,y_train)
    predictions = model.predict(X)
    return predictions