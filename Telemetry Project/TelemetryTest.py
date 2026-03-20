#Assertion test for Telemetry.py
from Telemetry import checkSignalIntegrity

# Test passing case
def testSignalLogic():
    assert checkSignalIntegrity(-35) == "STRONG" 

# Test failing case
def testWeakSignal():
    assert checkSignalIntegrity(-105) == "WEAK" 