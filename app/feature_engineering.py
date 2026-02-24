import re
from collections import defaultdict
from .ran_failure_patterns import FAILURE_PATTERNS

def extract_window_features(log_window):
    counters = defaultdict(int)

    for log in log_window:
       log_lower = log.lower()
       for key, pattern in FAILURE_PATTERNS.items():    
            if re.search(pattern, log_lower):
                counters[key] += 1

    return list(counters.values())