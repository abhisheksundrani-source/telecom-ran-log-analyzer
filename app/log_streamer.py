def stream_logs(file_path):
        """Stream large log files line-by-line."""
        with open(file_path, "r") as f:
                for line in f:
                        yield line.strip()