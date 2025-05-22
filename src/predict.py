import joblib
import numpy as np

model_path = "models/heart_risk_model.pkl"
model = joblib.load(model_path)

sample = np.array([[55,1,10,233,140,90,25.3,75,80]])
prediction = model.predict(sample)[0]
probablity = model.predict_proba(sample)[0][1]

label = "At Risk" if prediction == 1 else "Not at Risk"
print(f"Prediction: {label} ({probablity *100:.2f})% probablity")