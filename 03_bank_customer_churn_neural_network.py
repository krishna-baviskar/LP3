# Bank customer churn prediction with an MLP neural-network classifier.
import os, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

if os.path.exists("bank.csv"):
    df=pd.read_csv("bank.csv")
    target="Exited" if "Exited" in df.columns else "churn"
    y=df[target]; X=df.drop(columns=[target])
else:
    rng=np.random.default_rng(3); n=800
    age=rng.integers(18,80,n); balance=rng.uniform(0,200000,n)
    tenure=rng.integers(0,11,n); products=rng.integers(1,5,n)
    geography=rng.choice(["France","Spain","Germany"],n)
    gender=rng.choice(["Female","Male"],n)
    logit=-3+0.035*(age-40)+0.000012*balance+0.45*(products==1)+0.7*(geography=="Germany")
    prob=1/(1+np.exp(-logit)); y=(rng.random(n)<prob).astype(int)
    X=pd.DataFrame({"Age":age,"Balance":balance,"Tenure":tenure,"NumOfProducts":products,
                    "Geography":geography,"Gender":gender})
numeric=X.select_dtypes(include=np.number).columns.tolist()
categorical=[c for c in X.columns if c not in numeric]
prep=ColumnTransformer([
 ("num",make_pipeline(SimpleImputer(strategy="median"),StandardScaler()),numeric),
 ("cat",make_pipeline(SimpleImputer(strategy="most_frequent"),OneHotEncoder(handle_unknown="ignore")),categorical)])
model=make_pipeline(prep,MLPClassifier(hidden_layer_sizes=(32,16),max_iter=600,random_state=42,early_stopping=True))
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
model.fit(Xtr,ytr); pred=model.predict(Xte)
print("Accuracy:",round(accuracy_score(yte,pred),3))
print(classification_report(yte,pred,zero_division=0))
