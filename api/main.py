from fastapi import FastAPI
from app.log_streamer import stream_logs
from app.analyzer import analyze_stream

app = FastAPI()

@app.post("/analyze")
def analyze(file_path: str):
    stream = stream_logs(file_path)
    result = analyze_stream(stream)
    return {"status": result}