import random
import datetime

FAILURE_TYPES = [
    "RRC_SETUP_FAILURE",
    "HANDOVER_FAILURE",
    "ATTACH_REJECT",
    "NGAP_RESET",
    "RADIO_LINK_FAILURE",
    "KERNEL_PANIC"
]

def generate_synthetic_log(scenario="sunny", duration=60):
    """
    Generate synthetic log lines for a given scenario.
    scenario: 'sunny' (normal), 'rainy' (stress), 'mixed'
    duration: number of minutes simulated
    """
    logs = []
    for minute in range(duration):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if scenario == "sunny":
            failures = random.choices(FAILURE_TYPES, k=random.randint(0,2))
        elif scenario == "rainy":
            failures = random.choices(FAILURE_TYPES, k=random.randint(5,15))
        elif scenario == "mixed":
            failures = random.choices(FAILURE_TYPES, k=random.randint(0,8))
        else:
            failures = []

        for f in failures:
            logs.append(f"{timestamp} - {f}")
    return logs

def design_test_case(scenario, expected_outcome):
    """
    Define a test case with scenario and expected PASS/FAIL.
    """
    return {
        "scenario": scenario,
        "expected": expected_outcome,
        "logs": generate_synthetic_log(scenario)
    }
