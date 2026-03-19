# 🚀 telecom-ran-log-analyzer
AI-based anomaly detection system for telecom RAN log analysis using streaming and window-based ML detection.  
Designed for integration into test automation frameworks and CI/CD pipelines.

---

## 📡 Overview
RAN (Radio Access Network) E2E tests can run for 6–12 hours, generating large log files.  
Failures typically appear as bursts rather than isolated events.

This project demonstrates a scalable, memory-efficient AI-driven system that:
- Streams large logs without loading them fully into memory
- Aggregates logs into processing windows
- Extracts telecom-specific failure frequencies
- Applies rule-based spike detection
- Uses Isolation Forest for anomaly detection
- Returns a simple **PASS / FAIL** result for automation systems

---

## 🏗 Architecture
```
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
```


---

## ✔ Key Design Principles
- Memory-efficient streaming (generator-based)
- Window-level analysis instead of raw log-level ML
- Hybrid rule-based + ML approach
- Automation-ready output
- API integration capability

---

## ❗ Problem Statement
In telecom RAN validation environments:
- Test executions run for long durations (6–12+ hours)
- Logs grow large (hundreds of MBs to GBs)
- Failures occur as bursts:
  - RRC Setup Failures
  - Handover Failures
  - Attach Rejects
  - NGAP/S1 Resets
  - Radio Link Failures (RLF)
- Manual log inspection is inefficient
- Static grep-based thresholds miss abnormal patterns

**Need:**  
Scalable log processing, intelligent anomaly detection, automation-friendly PASS/FAIL output.

---

## 🛠 Tech Stack
| Component        | Purpose                          |
|------------------|----------------------------------|
| Python 3.8+      | Core language                    |
| Scikit-learn     | Isolation Forest anomaly model   |
| NumPy            | Numerical computations           |
| FastAPI          | API layer                        |
| Generators       | Memory-efficient log streaming   |
| Window features  | Telecom-specific failure metrics |

---

## 📂 Project Structure
```
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
```

---

## ▶️ How to Run (Local Execution)
1. **Clone Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/telecom-ran-log-analyzer.git
   cd telecom-ran-log-analyzer
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run Analyzer**
   ```bash
   python run.py
4. **Output:**
   ```console
   Final Status: PASS
   ```
   or
   ```console
   Final Status: FAIL
   ```

---

## 🌐 API Usage (FastAPI)

**Start API server**
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

**Open in browser**
http://localhost:8000/docs

## API Example
- Request
  ```http
  POST /analyze
  Body:
  {
          "file_path": "sample_logs/ran_sample.log"
  }
  ```

- Response
  ```json
  {
          "status": "PASS"
  }
  ```

Integration ready for:
- CI/CD pipelines
- Robot Framework
- Pytest automation
- Jenkins / GitLab pipelines

---

## 📊 Detection Strategy
1️. **Failure Pattern Extraction**
- Tracks telecom-specific breakages:
- RRC Setup Failure
- Handover Failure
- Attach Reject
- NGAP Reset
- Radio Link Failure
- Kernel Panic

2️. **Window-Based Feature Aggregation**
- Logs are grouped into windows
- Failure frequencies are calculated per window
- Window-level features are passed to ML model

3️. **Hybrid Detection**
- Layer 1: Rule-based threshold detection
- Layer 2: Isolation Forest anomaly detection

This reduces false positives and improves reliability.

---

## 🖼 Screenshots
**Swagger API Interface**

<img src="https://github.com/user-attachments/assets/04f5d83b-9b40-42f7-ae18-e799352a7395" width="400">

**Sample Console Output**
```console
Processing log window...
Detected RRC spike...
Final Status: FAIL
```

---

## 📈 Key Highlights
- Memory-efficient streaming (suitable for half-day logs)
- Window-level ML improves stability
- Hybrid rule + ML detection
- Automation-ready design
- Clean modular architecture
- Easily extendable for:
        - Time-based windows
        - Drift detection,
        - Log template extraction,
        - Model persistence,
        - Docker deployment

---

## 🔮 Future Improvements
- Time-based sliding windows (5-minute buckets)
- Log template extraction (Drain algorithm)
- Online learning models
- Model persistence & retraining
- Drift detection across builds
- Prometheus metrics integration
- Kafka-based real-time streaming

---

## 🎯 Use Cases
- Telecom RAN validation
- 5G gNB log monitoring
- CI/CD log intelligence
- Automation framework integration
- Network anomaly research

---

## 🆕 Enhancement Log (March 19, 2026)
✨ **New Features Added**
- Synthetic Test Case Generator (app/test_case_generator.py)
- Generates telecom failure scenarios (Sunny, Rainy, Mixed).
- Produces synthetic logs when real logs are unavailable.
- Supports categories like RRC Setup Failures, Handover Failures, NGAP Resets, Radio Link Failures, Kernel Panics, Attach Rejects.
- FastAPI Endpoints
- /generate_test_case → Create synthetic scenarios with preview logs.
- /generate_and_analyze → Generate logs and immediately run anomaly detection (PASS/FAIL).
- /analyze → Analyze real log files via streaming.
- Models Organized (app/models/test_case_models.py)
- Pydantic schemas for request/response consistency.
- Clean separation of API and business logic.

🛠 **Analyzer Improvements**
- Added analyze_logs for direct synthetic log analysis.
- Refined detection strategy:
- Smaller window size for synthetic bursts.
- Rule-based checks across all failure categories.
- Isolation Forest applied whenever features exist.
- Fixed premature return "PASS" bug in analyze_stream.

🚀 **Codespaces Integration**
- Added devcontainer.json and Dockerfile for seamless GitHub Codespaces execution.
- Auto-install dependencies (pip install -r requirements.txt).
- Port forwarding for FastAPI (8000).

## 📊 Example API Workflow**
**Generate and Analyze Rainy Scenario**
```http
POST /generate_and_analyze
Body:
{
  "scenario": "rainy",
  "expected": "FAIL"
}
```

**Response**
```json
{
  "scenario": "rainy",
  "expected": "FAIL",
  "analysis_result": "FAIL",
  "logs_preview": [
    "2026-03-19 18:51:59 - RRC_SETUP_FAILURE",
    "2026-03-19 18:51:59 - HANDOVER_FAILURE",
    "2026-03-19 18:51:59 - KERNEL_PANIC",
    ...
  ]
}
```

---

## 🎯 Impact
- Framework now self-validates even without real logs.
- Enables scenario-driven test case design (Sunny vs Rainy).
- Produces automation-ready PASS/FAIL outputs for CI/CD.
- Clean modular architecture for future extensions.
