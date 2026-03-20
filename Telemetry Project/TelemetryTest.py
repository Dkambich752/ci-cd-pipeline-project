#Assertion test for Telemetry.py
from Telemetry import checkSignalIntegrity

# Test passing case
def testSignalLogic():
    assert checkSignalIntegrity(-50) == "STRONG" 

# Test failing case
def testWeakSignal():
    assert checkSignalIntegrity(-100) == "WEAK" 