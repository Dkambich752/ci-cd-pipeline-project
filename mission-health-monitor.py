import urllib.request
import os

def lambda_handler(event, context):

    # For now, we'll ping google to test the logic
    # In a real implementation, this would be your telemetry EC2
    target_url = "https://www.google.com"

    print(f"Pinging {target_url} to check telemetry health...")

    try:
        # Perform GET request to the URL
        response = urllib.request.urlopen(target_url, timeout=10)
        status = response.getcode()
        # Check if response status is 200 (OK)
        if status == 200:
            print(f"STATUS: HEALTHY. Mission system is online")
        else:
            raise Exception(f"System returned unexpected status: {status}")
        
    except Exception as e:
        print(f"STATUS: UNHEALTHY. Mission system is offline.")
        print(f"Error details: {e}")
        # In real-world application, this would trigger SNS Alert email
        raise e  # Re-raise exception to indicate failure in Lambda execution