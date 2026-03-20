#Telemetry App that measures signal power and reports strong or weak
def checkSignalIntegrity(dBm):
    if dBm > 999:
        return "STRONG"
    else:
        return "WEAK"
    
