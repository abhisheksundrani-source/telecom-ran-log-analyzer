🚀 telecom-ran-log-analyzer
AI-based anomaly detection system for telecom RAN log analysis using streaming and window-based ML detection.
Designed for integration into test automation frameworks and CI/CD pipelines.

📡 Overview
RAN (Radio Access Network) E2E tests can run for 6–12 hours, generating large log files.
Failures typically appear as bursts rather than isolated events.
This project demonstrates a scalable, memory-efficient AI-driven system that:
Streams large logs without loading them fully into memory
Aggregates logs into processing windows
Extracts telecom-specific failure frequencies
Applies rule-based spike detection
Uses Isolation Forest for anomaly detection
Returns a simple PASS / FAIL result for automation systems

🏗 Architecture
Large RAN Logs (6–12 hrs)
        ↓
Generator-Based Streaming
        ↓
Window Aggregation
        ↓
Failure Frequency Extraction
        ↓
Rule-Based Spike Detection
        ↓
Isolation Forest (Window-Level)
        ↓
PASS / FAIL

Key Design Principles
✔ Memory-efficient streaming (generator-based)
✔ Window-level analysis instead of raw log-level ML
✔ Hybrid rule-based + ML approach
✔ Automation-ready output
✔ API integration capability

❗ Problem Statement
In telecom RAN validation environments:
Test executions run for long durations (6–12+ hours)
Logs grow large (hundreds of MBs to GBs)
Failures occur as bursts:
RRC Setup Failures
Handover Failures
Attach Rejects
NGAP/S1 Resets
Radio Link Failures (RLF)
Manual log inspection is inefficient
Static grep-based thresholds miss abnormal patterns
There is a need for:
Scalable log processing
Intelligent anomaly detection
Automation-friendly PASS/FAIL output

🛠 Tech Stack
Python 3.8+
Scikit-learn (Isolation Forest)
NumPy
FastAPI (API layer)
Generator-based streaming
Window-based feature engineering

📂 Project Structure
telecom-ran-log-analyzer/
│
├── app/
│   ├── log_streamer.py
│   ├── feature_engineering.py
│   ├── anomaly_model.py
│   ├── ran_failure_patterns.py
│   └── analyzer.py
│
├── api/
│   └── main.py
│
├── sample_logs/
│   └── ran_sample.log
│
├── run.py
├── requirements.txt
└── README.md

▶️ How to Run (Local Execution)
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/telecom-ran-log-analyzer.git
cd telecom-ran-log-analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Analyzer
python run.py
Output:
Final Status: PASS
or
Final Status: FAIL

🌐 API Usage (FastAPI)
Start API server:
uvicorn api.main:app --host 0.0.0.0 --port 8000
Open in browser:
http://localhost:8000/docs


