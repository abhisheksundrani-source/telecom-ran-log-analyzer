from fastapi import FastAPI
from app.log_streamer import stream_logs
from app.analyzer import analyze_stream
from pydantic import BaseModel
from app.test_case_generator import design_test_case
from app.models.test_case_models import TestCaseRequest, TestCaseResponse

app = FastAPI()

@app.post("/analyze")
def analyze(file_path: str):
    stream = stream_logs(file_path)
    result = analyze_stream(stream)
    return {"status": result}

@app.post("/generate_test_case", response_model=TestCaseResponse)
def generate_test_case(req: TestCaseRequest):
    tc = design_test_case(req.scenario, req.expected)
    return TestCaseResponse(
        scenario=tc["scenario"],
        expected=tc["expected"],
        logs=tc["logs"][:50]  # preview first 50 lines
    )

@app.post("/generate_and_analyze")
def generate_and_analyze(req: TestCaseRequest):
    tc = design_test_case(req.scenario, req.expected)
    result = analyze_logs(tc["logs"])   # run anomaly detection
    return {
        "scenario": tc["scenario"],
        "expected": tc["expected"],
        "analysis_result": result,      # PASS/FAIL from model
        "logs_preview": tc["logs"][:50]
    }