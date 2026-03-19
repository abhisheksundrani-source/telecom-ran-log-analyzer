from pydantic import BaseModel
from typing import List

class TestCaseRequest(BaseModel):
    scenario: str   # e.g. "sunny", "rainy", "mixed"
    expected: str   # e.g. "PASS" or "FAIL"

class TestCaseResponse(BaseModel):
    scenario: str
    expected: str
    logs: List[str]