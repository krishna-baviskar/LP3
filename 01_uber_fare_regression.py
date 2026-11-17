# Uber fare prediction: uses a CSV with pickup_longitude, pickup_latitude,
# dropoff_longitude, dropoff_latitude, passenger_count, fare_amount.
# If no CSV is supplied, a small synthetic dataset is generated for demonstration.
import os, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

path = "uber.csv"
if os.path.exists(path):
    df = pd.read_csv(path)
else:
    rng=np.random.default_rng(7); n=1000
    plon=rng.uniform(-74.05,-73.75,n); plat=rng.uniform(40.60,40.90,n)
    dlon=rng.uniform(-74.05,-73.75,n); dlat=rng.uniform(40.60,40.90,n)
    dist=np.sqrt((plon-dlon)**2+(plat-dlat)**2)*70
    df=pd.DataFrame({"pickup_longitude":plon,"pickup_latitude":plat,
      "dropoff_longitude":dlon,"dropoff_latitude":dlat,
      "passenger_count":rng.integers(1,6,n),
      "fare_amount":3+2.2*dist+rng.normal(0,2,n)})
features=["pickup_longitude","pickup_latitude","dropoff_longitude",
          "dropoff_latitude","passenger_count"]
df=df[features+["fare_amount"]].replace([np.inf,-np.inf],np.nan).dropna(subset=["fare_amount"])
X_train,X_test,y_train,y_test=train_test_split(df[features],df.fare_amount,test_size=.2,random_state=42)
models={"Linear Regression":make_pipeline(SimpleImputer(),StandardScaler(),LinearRegression()),
        "Random Forest":make_pipeline(SimpleImputer(),RandomForestRegressor(n_estimators=150,random_state=42))}
for name,model in models.items():
    model.fit(X_train,y_train); pred=model.predict(X_test)
    rmse=np.sqrt(mean_squared_error(y_test,pred))
    print(f"{name}: R2={r2_score(y_test,pred):.3f}, RMSE={rmse:.3f}")
print("Note: replace uber.csv with the actual cleaned dataset for real results.")
