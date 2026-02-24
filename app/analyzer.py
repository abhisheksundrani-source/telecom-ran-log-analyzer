from .feature_engineering import extract_window_features
from .anomaly_model import detect_window_anomalies

def analyze_stream(log_stream, window_size=200):
    window = []
    all_features = []

    for log in log_stream:
        window.append(log)

        if len(window) >= window_size:
            features = extract_window_features(window)
            all_features.append(features)
                
            # Rule-based check
            if len(features) > 0 and features[0] > 50:
                return "FAIL"

            window = []

        if len(all_features) > 3:
            preds = detect_window_anomalies(all_features)
            if any(p == -1 for p in preds):                   
                return "FAIL"

        return "PASS"