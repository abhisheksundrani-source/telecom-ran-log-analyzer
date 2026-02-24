from app.log_streamer import stream_logs
from app.analyzer import analyze_stream

if __name__ == "__main__":
    stream = stream_logs("sample_logs/ran_sample.log")
    result = analyze_stream(stream)
    print("Final Status:", result)