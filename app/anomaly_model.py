from sklearn.ensemble import IsolationForest
import numpy as np

def detect_window_anomalies(window_features):
    X = np.array(window_features)

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)

    preds = model.predict(X)   
    return preds